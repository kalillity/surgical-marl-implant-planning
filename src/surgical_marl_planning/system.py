import torch
from torch import Tensor, nn

from surgical_marl_planning.models.communication import GatedCrossAttention
from surgical_marl_planning.models.encoders import (
    BiomechanicalEncoder,
    SegmentationEncoder,
    VectorEncoder,
    VerifierEncoder,
)
from surgical_marl_planning.training.happo import CentralizedCritic, GaussianPolicy
from surgical_marl_planning.types import AgentActions, AgentObservations, PlanResult


class SurgicalPlanningSystem(nn.Module):
    def __init__(
        self,
        latent_dim: int = 256,
        design_dim: int = 16,
        trajectory_dim: int = 12,
        plan_dim: int = 128,
    ) -> None:
        super().__init__()
        self.segmentation = SegmentationEncoder(latent_dim, channels=(16, 32, 64, 128))
        self.biomechanical = BiomechanicalEncoder(latent_dim=latent_dim)
        self.designer = VectorEncoder(design_dim, latent_dim)
        self.planner = VectorEncoder(trajectory_dim, latent_dim)
        self.plan_projection = VectorEncoder(plan_dim, latent_dim, 512, 4)
        self.verifier = VerifierEncoder(latent_dim)
        self.communication = GatedCrossAttention(latent_dim)
        action_dimensions = (8, 8, 16, 12, 3)
        self.policies = nn.ModuleList(GaussianPolicy(latent_dim, dim) for dim in action_dimensions)
        self.critic = CentralizedCritic(latent_dim)

    def encode(
        self, observations: AgentObservations
    ) -> tuple[
        tuple[Tensor, Tensor, Tensor, Tensor, Tensor],
        Tensor,
        Tensor,
        Tensor,
    ]:
        segmentation_state, mask, uncertainty = self.segmentation(observations.volume)
        biomechanical_state, stress = self.biomechanical(
            observations.mesh.node_features,
            observations.mesh.edge_index,
            observations.mesh.batch_index,
        )
        design_state = self.designer(observations.design)
        trajectory_state = self.planner(observations.trajectory)
        verifier_input = torch.stack(
            (
                segmentation_state,
                biomechanical_state,
                design_state,
                trajectory_state,
                self.plan_projection(observations.plan_state),
            ),
            dim=1,
        )
        verifier_state, _, _ = self.verifier(verifier_input)
        states = (
            segmentation_state,
            biomechanical_state,
            design_state,
            trajectory_state,
            verifier_state,
        )
        return states, mask, uncertainty, stress

    def forward(
        self,
        observations: AgentObservations,
        deterministic: bool = False,
        max_revisions: int = 3,
    ) -> PlanResult:
        states, mask, _, stress = self.encode(observations)
        last_gates = states[0].new_zeros(states[0].shape[0], 5, 5, 4)
        actions: tuple[Tensor, Tensor, Tensor, Tensor, Tensor] | None = None
        accepted = torch.zeros(states[0].shape[0], dtype=torch.bool, device=states[0].device)
        revisions = max_revisions
        for revision in range(max_revisions):
            states, last_gates, _ = self.communication(states)
            sampled = tuple(
                policy(state, deterministic)[0]
                for policy, state in zip(self.policies, states, strict=True)
            )
            actions = (sampled[0], sampled[1], sampled[2], sampled[3], sampled[4])
            accepted = actions[4].argmax(-1) == 0
            if bool(accepted.all()):
                revisions = revision
                break
            feedback = torch.tanh(actions[4].mean(-1, keepdim=True))
            states = (
                states[0],
                states[1],
                states[2],
                states[3] + feedback,
                states[4],
            )
        if actions is None:
            raise RuntimeError("max_revisions must be positive")
        packaged = AgentActions(mask, stress, actions[2], actions[3], actions[4])
        return PlanResult(packaged, accepted, revisions, last_gates)
