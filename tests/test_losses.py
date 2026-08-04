import torch

from surgical_marl_planning.losses.objectives import ConstrainedReward
from surgical_marl_planning.types import ConstraintTerms, RewardTerms


def reward_terms(value: float) -> RewardTerms:
    tensor = torch.full((4,), value)
    return RewardTerms(tensor, tensor, tensor, tensor, tensor)


def constraint_terms(value: float) -> ConstraintTerms:
    tensor = torch.full((4,), value)
    return ConstraintTerms(tensor, tensor, tensor, tensor)


def test_reward_without_violation() -> None:
    objective = ConstrainedReward()
    output = objective(reward_terms(1.0), constraint_terms(0.0))
    assert torch.allclose(output.objective, torch.ones(4))


def test_reward_penalizes_four_constraints() -> None:
    objective = ConstrainedReward()
    output = objective(reward_terms(1.0), constraint_terms(0.25))
    assert torch.allclose(output.penalty, torch.ones(4))
    assert torch.allclose(output.objective, torch.zeros(4))


def test_dual_step_increases_multipliers() -> None:
    objective = ConstrainedReward(dual_rate=0.1)
    previous = objective.multipliers.clone()
    current = objective.dual_step(torch.ones(8, 4))
    assert torch.all(current > previous)


def test_negative_constraints_are_inactive() -> None:
    objective = ConstrainedReward()
    output = objective(reward_terms(1.0), constraint_terms(-1.0))
    assert torch.equal(output.violations, torch.zeros(4, 4))
