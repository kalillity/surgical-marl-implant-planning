import math
from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingPhase:
    cooperative: bool
    adversarial_weight: float
    learning_rate_scale: float


def training_phase(
    epoch: int,
    total_epochs: int = 500,
    cooperative_fraction: float = 0.6,
    warmup_fraction: float = 0.05,
) -> TrainingPhase:
    if not 0 <= epoch < total_epochs:
        raise ValueError("epoch outside training range")
    cooperative_end = int(total_epochs * cooperative_fraction)
    cooperative = epoch < cooperative_end
    adversarial_weight = 0.0
    if not cooperative:
        adversarial_weight = (epoch - cooperative_end) / max(total_epochs - cooperative_end - 1, 1)
    warmup_epochs = max(int(total_epochs * warmup_fraction), 1)
    if epoch < warmup_epochs:
        scale = (epoch + 1) / warmup_epochs
    else:
        progress = (epoch - warmup_epochs) / max(total_epochs - warmup_epochs - 1, 1)
        scale = 0.5 * (1 + math.cos(math.pi * progress))
    return TrainingPhase(cooperative, adversarial_weight, scale)
