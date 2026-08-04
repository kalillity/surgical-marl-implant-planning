from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass(frozen=True)
class Interval:
    estimate: float
    lower: float
    upper: float


def bootstrap_interval(
    values: NDArray[np.float64],
    confidence: float = 0.95,
    samples: int = 10000,
    seed: int = 42,
) -> Interval:
    if values.ndim != 1 or values.size < 2:
        raise ValueError("values must be a one-dimensional sample with at least two entries")
    generator = np.random.default_rng(seed)
    indices = generator.integers(0, values.size, size=(samples, values.size))
    estimates = values[indices].mean(axis=1)
    alpha = 1 - confidence
    return Interval(
        float(values.mean()),
        float(np.quantile(estimates, alpha / 2)),
        float(np.quantile(estimates, 1 - alpha / 2)),
    )


def paired_effect_size(left: NDArray[np.float64], right: NDArray[np.float64]) -> float:
    difference = left - right
    deviation = difference.std(ddof=1)
    if deviation == 0:
        return float("inf")
    return float(difference.mean() / deviation)


def mcid_crossing_rate(
    baseline: NDArray[np.float64], candidate: NDArray[np.float64], threshold: float
) -> float:
    if baseline.shape != candidate.shape:
        raise ValueError("paired arrays must share a shape")
    return float(np.mean((baseline - candidate) >= threshold))
