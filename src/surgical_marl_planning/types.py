from dataclasses import dataclass
from enum import IntEnum

from torch import Tensor


class AgentId(IntEnum):
    SEGMENTATION = 0
    BIOMECHANICAL = 1
    DESIGNER = 2
    PLANNER = 3
    VERIFIER = 4


@dataclass(frozen=True)
class MeshBatch:
    node_features: Tensor
    edge_index: Tensor
    batch_index: Tensor


@dataclass(frozen=True)
class AgentObservations:
    volume: Tensor
    mesh: MeshBatch
    design: Tensor
    trajectory: Tensor
    plan_state: Tensor


@dataclass(frozen=True)
class AgentActions:
    segmentation: Tensor
    stress: Tensor
    design: Tensor
    trajectory: Tensor
    verification: Tensor


@dataclass(frozen=True)
class RewardTerms:
    segmentation: Tensor
    stress: Tensor
    feasibility: Tensor
    trajectory: Tensor
    verification: Tensor


@dataclass(frozen=True)
class ConstraintTerms:
    stress: Tensor
    collision: Tensor
    reachability: Tensor
    manufacturability: Tensor


@dataclass(frozen=True)
class CommunicationResult:
    states: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    gates: Tensor
    attention: Tensor


@dataclass(frozen=True)
class PlanResult:
    actions: AgentActions
    accepted: Tensor
    revisions: int
    gates: Tensor


@dataclass(frozen=True)
class TransitionBatch:
    observations: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    actions: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    log_probabilities: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    advantages: Tensor
    returns: Tensor
    values: Tensor
