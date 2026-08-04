import torch

from surgical_marl_planning.models.communication import TOPOLOGY, GatedCrossAttention


def test_communication_shapes() -> None:
    module = GatedCrossAttention(32, 4)
    states = tuple(torch.randn(2, 32) for _ in range(5))
    updated, gates, attention = module(states)
    assert len(updated) == 5
    assert all(value.shape == (2, 32) for value in updated)
    assert gates.shape == (2, 5, 5, 4)
    assert attention.shape == (2, 5, 5, 4)


def test_inactive_topology_has_zero_gate() -> None:
    module = GatedCrossAttention(32, 4)
    states = tuple(torch.randn(2, 32) for _ in range(5))
    _, gates, _ = module(states)
    for source in range(5):
        for target in range(5):
            if not TOPOLOGY[source][target]:
                assert torch.equal(gates[:, source, target], torch.zeros(2, 4))


def test_active_gates_are_probabilities() -> None:
    module = GatedCrossAttention(32, 4)
    states = tuple(torch.randn(2, 32) for _ in range(5))
    _, gates, _ = module(states)
    active = torch.tensor(TOPOLOGY).unsqueeze(0).unsqueeze(-1).expand_as(gates)
    assert torch.all(gates[active] > 0)
    assert torch.all(gates[active] < 1)
