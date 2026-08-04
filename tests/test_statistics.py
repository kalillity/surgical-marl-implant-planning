import numpy as np

from surgical_marl_planning.evaluation.statistics import (
    bootstrap_interval,
    mcid_crossing_rate,
    paired_effect_size,
)


def test_bootstrap_interval_contains_mean() -> None:
    values = np.arange(10, dtype=np.float64)
    interval = bootstrap_interval(values, samples=500)
    assert interval.lower < interval.estimate < interval.upper


def test_paired_effect_size_positive() -> None:
    left = np.array([5.0, 7.0, 8.0])
    right = np.array([4.0, 5.5, 7.5])
    assert paired_effect_size(left, right) > 0


def test_mcid_rate() -> None:
    baseline = np.array([3.0, 2.0, 4.0])
    candidate = np.array([1.0, 1.5, 2.0])
    assert mcid_crossing_rate(baseline, candidate, 1.0) == 2 / 3
