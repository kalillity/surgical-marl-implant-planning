from surgical_marl_planning.evaluation.benchmark_catalog import PROTOCOLS, select_protocols


def test_catalog_size_regression() -> None:
    assert len(PROTOCOLS) == 180


def test_catalog_identifiers_are_unique() -> None:
    identifiers = {protocol.identifier for protocol in PROTOCOLS}
    assert len(identifiers) == len(PROTOCOLS)


def test_catalog_selection() -> None:
    selected = select_protocols(85.0, 4.0)
    assert all(protocol.expected_composite >= 85.0 for protocol in selected)
    assert all(protocol.expected_failure <= 4.0 for protocol in selected)


def test_catalog_resource_estimates() -> None:
    assert all(protocol.gpu_hours > 0 for protocol in PROTOCOLS)
    assert all(protocol.effective_samples > 0 for protocol in PROTOCOLS)


def test_catalog_agent_range() -> None:
    assert min(protocol.agents for protocol in PROTOCOLS) == 3
    assert max(protocol.agents for protocol in PROTOCOLS) == 7


def test_catalog_data_fractions() -> None:
    fractions = {protocol.data_fraction for protocol in PROTOCOLS}
    assert fractions == {0.1, 0.25, 0.5, 1.0}
