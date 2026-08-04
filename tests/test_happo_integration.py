import torch

from surgical_marl_planning.training.happo import (
    CentralizedCritic,
    GaussianPolicy,
    HAPPOUpdater,
    PolicyBatch,
)


def test_sequential_policy_update_changes_parameters() -> None:
    policies = [GaussianPolicy(8, 2) for _ in range(5)]
    critic = CentralizedCritic(8)
    updater = HAPPOUpdater(policies, critic)
    states = tuple(torch.randn(4, 8) for _ in range(5))
    sampled = tuple(policy(state) for policy, state in zip(policies, states, strict=True))
    actions = tuple(value[0].detach() for value in sampled)
    probabilities = tuple(value[1].detach() for value in sampled)
    with torch.no_grad():
        values = critic(states)
    batch = PolicyBatch(
        states,
        actions,
        probabilities,
        torch.ones(4),
        values + 1,
        values,
    )
    previous = policies[0].mean[0].weight.detach().clone()
    losses = updater.update(batch)
    current = policies[0].mean[0].weight.detach()
    assert set(losses) == {"actor_0", "actor_1", "actor_2", "actor_3", "actor_4", "critic"}
    assert not torch.equal(previous, current)
