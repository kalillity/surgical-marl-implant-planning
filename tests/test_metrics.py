import torch

from surgical_marl_planning.metrics.clinical import (
    angular_error,
    composite_score,
    dice_score,
    generalization_gap,
    threshold_pass,
    trajectory_deviation,
)


def test_dice_identity() -> None:
    target = torch.ones(2, 1, 4, 4, 4)
    assert torch.allclose(dice_score(target, target), torch.ones(2))


def test_dice_disjoint() -> None:
    prediction = torch.zeros(2, 1, 4, 4, 4)
    target = torch.ones_like(prediction)
    assert torch.all(dice_score(prediction, target) < 1e-5)


def test_trajectory_identity() -> None:
    trajectory = torch.tensor([[0.0, 0.0, 0.0, 1.0, 0.0, 0.0]])
    assert torch.equal(trajectory_deviation(trajectory, trajectory), torch.zeros(1))


def test_angular_right_angle() -> None:
    left = torch.tensor([[0.0, 0.0, 0.0, 1.0, 0.0, 0.0]])
    right = torch.tensor([[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]])
    assert torch.allclose(angular_error(left, right), torch.tensor([90.0]))


def test_composite_weighting() -> None:
    values = torch.ones(3)
    assert torch.allclose(composite_score(values, values, values, values, values), values * 100)


def test_generalization_thresholds() -> None:
    gap = generalization_gap(torch.tensor(87.3), torch.tensor(82.0))
    assert bool(threshold_pass(gap, "dataset"))
    assert bool(threshold_pass(gap, "site"))
    assert bool(threshold_pass(gap, "pathology"))
    assert bool(threshold_pass(gap, "demographic"))
