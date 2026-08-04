from dataclasses import dataclass
from typing import cast

import torch
from torch import Tensor


@dataclass(frozen=True)
class PlanMetrics:
    dice: Tensor
    trajectory_deviation: Tensor
    angular_error: Tensor
    collision_rate: Tensor
    stress_safety: Tensor
    design_feasibility: Tensor
    verification_pass: Tensor
    composite: Tensor


def dice_score(prediction: Tensor, target: Tensor, epsilon: float = 1e-6) -> Tensor:
    prediction = prediction.flatten(start_dim=1)
    target = target.flatten(start_dim=1)
    intersection = (prediction * target).sum(-1)
    return (2 * intersection + epsilon) / (prediction.sum(-1) + target.sum(-1) + epsilon)


def trajectory_deviation(prediction: Tensor, target: Tensor) -> Tensor:
    entry = torch.linalg.vector_norm(prediction[:, :3] - target[:, :3], dim=-1)
    tip = torch.linalg.vector_norm(prediction[:, 3:6] - target[:, 3:6], dim=-1)
    return cast(Tensor, (entry + tip) * 0.5)


def angular_error(prediction: Tensor, target: Tensor) -> Tensor:
    predicted_direction = prediction[:, 3:6] - prediction[:, :3]
    target_direction = target[:, 3:6] - target[:, :3]
    cosine = torch.nn.functional.cosine_similarity(predicted_direction, target_direction).clamp(
        -1, 1
    )
    return torch.rad2deg(torch.acos(cosine))


def composite_score(
    dice: Tensor,
    stress_safety: Tensor,
    feasibility: Tensor,
    trajectory_accuracy: Tensor,
    verification: Tensor,
) -> Tensor:
    return 100 * (
        0.15 * dice
        + 0.20 * stress_safety
        + 0.20 * feasibility
        + 0.25 * trajectory_accuracy
        + 0.20 * verification
    )


def generalization_gap(training_score: Tensor, test_score: Tensor) -> Tensor:
    return (training_score - test_score).abs()


def threshold_pass(gap: Tensor, axis: str) -> Tensor:
    thresholds = {"dataset": 8.0, "site": 12.0, "pathology": 15.0, "demographic": 10.0}
    if axis not in thresholds:
        raise ValueError(f"unknown generalization axis: {axis}")
    return gap < thresholds[axis]
