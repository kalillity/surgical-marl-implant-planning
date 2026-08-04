import pytest

from surgical_marl_planning.training.schedule import training_phase


def test_cooperative_phase() -> None:
    phase = training_phase(0)
    assert phase.cooperative
    assert phase.adversarial_weight == 0
    assert phase.learning_rate_scale > 0


def test_adversarial_phase() -> None:
    phase = training_phase(400)
    assert not phase.cooperative
    assert 0 < phase.adversarial_weight < 1


def test_last_epoch_cosine_decay() -> None:
    phase = training_phase(499)
    assert phase.learning_rate_scale == 0


def test_invalid_epoch() -> None:
    with pytest.raises(ValueError):
        training_phase(500)


@pytest.mark.parametrize(
    ("epoch", "cooperative"),
    (
        (0, True),
        (24, True),
        (25, True),
        (299, True),
        (300, False),
        (350, False),
        (499, False),
    ),
)
def test_phase_boundary_regression(epoch: int, cooperative: bool) -> None:
    assert training_phase(epoch).cooperative is cooperative


@pytest.mark.parametrize("epoch", (0, 24, 25, 100, 299, 300, 400, 499))
def test_learning_rate_scale_is_bounded(epoch: int) -> None:
    scale = training_phase(epoch).learning_rate_scale
    assert 0 <= scale <= 1
