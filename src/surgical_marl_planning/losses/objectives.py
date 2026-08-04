from dataclasses import dataclass

import torch
from torch import Tensor, nn

from surgical_marl_planning.types import ConstraintTerms, RewardTerms


@dataclass(frozen=True)
class RewardOutput:
    objective: Tensor
    cooperative: Tensor
    penalty: Tensor
    violations: Tensor


class ConstrainedReward(nn.Module):
    weights: Tensor
    multipliers: Tensor

    def __init__(
        self,
        weights: tuple[float, float, float, float, float] = (0.15, 0.20, 0.20, 0.25, 0.20),
        dual_rate: float = 5e-3,
    ) -> None:
        super().__init__()
        self.register_buffer("weights", torch.tensor(weights))
        self.register_buffer("multipliers", torch.ones(4))
        self.dual_rate = dual_rate

    def forward(self, rewards: RewardTerms, constraints: ConstraintTerms) -> RewardOutput:
        terms = torch.stack(
            (
                rewards.segmentation,
                rewards.stress,
                rewards.feasibility,
                rewards.trajectory,
                rewards.verification,
            ),
            dim=-1,
        )
        violations = torch.stack(
            (
                constraints.stress,
                constraints.collision,
                constraints.reachability,
                constraints.manufacturability,
            ),
            dim=-1,
        ).clamp_min(0)
        cooperative = (terms * self.weights).sum(-1)
        penalty = (violations * self.multipliers).sum(-1)
        return RewardOutput(cooperative - penalty, cooperative, penalty, violations)

    @torch.no_grad()
    def dual_step(self, violations: Tensor) -> Tensor:
        update = self.dual_rate * violations.mean(0)
        self.multipliers.add_(update).clamp_(min=0)
        return self.multipliers.clone()


class ClippedPolicyObjective(nn.Module):
    def __init__(self, clip_ratio: float = 0.2, entropy_weight: float = 0.01) -> None:
        super().__init__()
        self.clip_ratio = clip_ratio
        self.entropy_weight = entropy_weight

    def forward(
        self,
        new_log_probability: Tensor,
        old_log_probability: Tensor,
        advantage: Tensor,
        entropy: Tensor,
    ) -> Tensor:
        ratio = torch.exp(new_log_probability - old_log_probability)
        direct = ratio * advantage
        clipped = ratio.clamp(1 - self.clip_ratio, 1 + self.clip_ratio) * advantage
        return -torch.minimum(direct, clipped).mean() - self.entropy_weight * entropy.mean()


class ClippedValueObjective(nn.Module):
    def __init__(self, clip_ratio: float = 0.2) -> None:
        super().__init__()
        self.clip_ratio = clip_ratio

    def forward(self, prediction: Tensor, previous: Tensor, target: Tensor) -> Tensor:
        clipped = previous + (prediction - previous).clamp(-self.clip_ratio, self.clip_ratio)
        direct = (prediction - target).square()
        limited = (clipped - target).square()
        return 0.5 * torch.maximum(direct, limited).mean()
