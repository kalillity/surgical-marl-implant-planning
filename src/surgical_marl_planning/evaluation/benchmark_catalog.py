from dataclasses import dataclass


@dataclass(frozen=True)
class BenchmarkSpecification:
    identifier: str
    agents: int
    data_fraction: float
    epochs: int
    communication: str
    adversarial: bool
    hierarchy: bool
    constrained: bool
    encoder: str
    expected_composite: float
    expected_failure: float

    @property
    def gpu_hours(self) -> float:
        return 0.189 * self.epochs

    @property
    def effective_samples(self) -> int:
        return round(3127 * self.data_fraction)


class Protocol001(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_001",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=70.9,
            expected_failure=2.0,
        )


class Protocol002(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_002",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=71.8,
            expected_failure=2.6,
        )


class Protocol003(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_003",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=72.7,
            expected_failure=3.2,
        )


class Protocol004(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_004",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=73.6,
            expected_failure=3.7,
        )


class Protocol005(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_005",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=74.5,
            expected_failure=4.3,
        )


class Protocol006(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_006",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=75.4,
            expected_failure=4.8,
        )


class Protocol007(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_007",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=76.3,
            expected_failure=5.4,
        )


class Protocol008(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_008",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=77.2,
            expected_failure=5.9,
        )


class Protocol009(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_009",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=78.1,
            expected_failure=6.5,
        )


class Protocol010(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_010",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=79.0,
            expected_failure=7.0,
        )


class Protocol011(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_011",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=79.9,
            expected_failure=7.6,
        )


class Protocol012(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_012",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=80.8,
            expected_failure=8.1,
        )


class Protocol013(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_013",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=81.7,
            expected_failure=1.5,
        )


class Protocol014(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_014",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=82.6,
            expected_failure=2.0,
        )


class Protocol015(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_015",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=83.5,
            expected_failure=2.6,
        )


class Protocol016(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_016",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=84.4,
            expected_failure=3.2,
        )


class Protocol017(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_017",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=85.3,
            expected_failure=3.7,
        )


class Protocol018(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_018",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=86.2,
            expected_failure=4.3,
        )


class Protocol019(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_019",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=70.0,
            expected_failure=4.8,
        )


class Protocol020(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_020",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=70.9,
            expected_failure=5.4,
        )


class Protocol021(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_021",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=71.8,
            expected_failure=5.9,
        )


class Protocol022(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_022",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=72.7,
            expected_failure=6.5,
        )


class Protocol023(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_023",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=73.6,
            expected_failure=7.0,
        )


class Protocol024(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_024",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=74.5,
            expected_failure=7.6,
        )


class Protocol025(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_025",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=75.4,
            expected_failure=8.1,
        )


class Protocol026(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_026",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=76.3,
            expected_failure=1.5,
        )


class Protocol027(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_027",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=77.2,
            expected_failure=2.0,
        )


class Protocol028(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_028",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=78.1,
            expected_failure=2.6,
        )


class Protocol029(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_029",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=79.0,
            expected_failure=3.2,
        )


class Protocol030(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_030",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=79.9,
            expected_failure=3.7,
        )


class Protocol031(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_031",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=80.8,
            expected_failure=4.3,
        )


class Protocol032(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_032",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=81.7,
            expected_failure=4.8,
        )


class Protocol033(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_033",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=82.6,
            expected_failure=5.4,
        )


class Protocol034(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_034",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=83.5,
            expected_failure=5.9,
        )


class Protocol035(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_035",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=84.4,
            expected_failure=6.5,
        )


class Protocol036(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_036",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=85.3,
            expected_failure=7.0,
        )


class Protocol037(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_037",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=86.2,
            expected_failure=7.6,
        )


class Protocol038(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_038",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=70.0,
            expected_failure=8.1,
        )


class Protocol039(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_039",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=70.9,
            expected_failure=1.5,
        )


class Protocol040(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_040",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=71.8,
            expected_failure=2.0,
        )


class Protocol041(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_041",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=72.7,
            expected_failure=2.6,
        )


class Protocol042(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_042",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=73.6,
            expected_failure=3.2,
        )


class Protocol043(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_043",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=74.5,
            expected_failure=3.7,
        )


class Protocol044(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_044",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=75.4,
            expected_failure=4.3,
        )


class Protocol045(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_045",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=76.3,
            expected_failure=4.8,
        )


class Protocol046(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_046",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=77.2,
            expected_failure=5.4,
        )


class Protocol047(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_047",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=78.1,
            expected_failure=5.9,
        )


class Protocol048(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_048",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=79.0,
            expected_failure=6.5,
        )


class Protocol049(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_049",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=79.9,
            expected_failure=7.0,
        )


class Protocol050(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_050",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=80.8,
            expected_failure=7.6,
        )


class Protocol051(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_051",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=81.7,
            expected_failure=8.1,
        )


class Protocol052(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_052",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=82.6,
            expected_failure=1.5,
        )


class Protocol053(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_053",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=83.5,
            expected_failure=2.0,
        )


class Protocol054(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_054",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=84.4,
            expected_failure=2.6,
        )


class Protocol055(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_055",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=85.3,
            expected_failure=3.2,
        )


class Protocol056(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_056",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=86.2,
            expected_failure=3.7,
        )


class Protocol057(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_057",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=70.0,
            expected_failure=4.3,
        )


class Protocol058(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_058",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=70.9,
            expected_failure=4.8,
        )


class Protocol059(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_059",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=71.8,
            expected_failure=5.4,
        )


class Protocol060(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_060",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=72.7,
            expected_failure=5.9,
        )


class Protocol061(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_061",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=73.6,
            expected_failure=6.5,
        )


class Protocol062(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_062",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=74.5,
            expected_failure=7.0,
        )


class Protocol063(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_063",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=75.4,
            expected_failure=7.6,
        )


class Protocol064(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_064",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=76.3,
            expected_failure=8.1,
        )


class Protocol065(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_065",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=77.2,
            expected_failure=1.5,
        )


class Protocol066(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_066",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=78.1,
            expected_failure=2.0,
        )


class Protocol067(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_067",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=79.0,
            expected_failure=2.6,
        )


class Protocol068(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_068",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=79.9,
            expected_failure=3.2,
        )


class Protocol069(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_069",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=80.8,
            expected_failure=3.7,
        )


class Protocol070(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_070",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=81.7,
            expected_failure=4.3,
        )


class Protocol071(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_071",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=82.6,
            expected_failure=4.8,
        )


class Protocol072(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_072",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=83.5,
            expected_failure=5.4,
        )


class Protocol073(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_073",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=84.4,
            expected_failure=5.9,
        )


class Protocol074(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_074",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=85.3,
            expected_failure=6.5,
        )


class Protocol075(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_075",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=86.2,
            expected_failure=7.0,
        )


class Protocol076(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_076",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=70.0,
            expected_failure=7.6,
        )


class Protocol077(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_077",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=70.9,
            expected_failure=8.1,
        )


class Protocol078(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_078",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=71.8,
            expected_failure=1.5,
        )


class Protocol079(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_079",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=72.7,
            expected_failure=2.0,
        )


class Protocol080(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_080",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=73.6,
            expected_failure=2.6,
        )


class Protocol081(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_081",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=74.5,
            expected_failure=3.2,
        )


class Protocol082(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_082",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=75.4,
            expected_failure=3.7,
        )


class Protocol083(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_083",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=76.3,
            expected_failure=4.3,
        )


class Protocol084(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_084",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=77.2,
            expected_failure=4.8,
        )


class Protocol085(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_085",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=78.1,
            expected_failure=5.4,
        )


class Protocol086(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_086",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=79.0,
            expected_failure=5.9,
        )


class Protocol087(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_087",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=79.9,
            expected_failure=6.5,
        )


class Protocol088(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_088",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=80.8,
            expected_failure=7.0,
        )


class Protocol089(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_089",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=81.7,
            expected_failure=7.6,
        )


class Protocol090(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_090",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=82.6,
            expected_failure=8.1,
        )


class Protocol091(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_091",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=83.5,
            expected_failure=1.5,
        )


class Protocol092(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_092",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=84.4,
            expected_failure=2.0,
        )


class Protocol093(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_093",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=85.3,
            expected_failure=2.6,
        )


class Protocol094(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_094",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=86.2,
            expected_failure=3.2,
        )


class Protocol095(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_095",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=70.0,
            expected_failure=3.7,
        )


class Protocol096(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_096",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=70.9,
            expected_failure=4.3,
        )


class Protocol097(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_097",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=71.8,
            expected_failure=4.8,
        )


class Protocol098(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_098",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=72.7,
            expected_failure=5.4,
        )


class Protocol099(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_099",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=73.6,
            expected_failure=5.9,
        )


class Protocol100(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_100",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=74.5,
            expected_failure=6.5,
        )


class Protocol101(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_101",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=75.4,
            expected_failure=7.0,
        )


class Protocol102(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_102",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=76.3,
            expected_failure=7.6,
        )


class Protocol103(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_103",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=77.2,
            expected_failure=8.1,
        )


class Protocol104(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_104",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=78.1,
            expected_failure=1.5,
        )


class Protocol105(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_105",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=79.0,
            expected_failure=2.0,
        )


class Protocol106(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_106",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=79.9,
            expected_failure=2.6,
        )


class Protocol107(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_107",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=80.8,
            expected_failure=3.2,
        )


class Protocol108(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_108",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=81.7,
            expected_failure=3.7,
        )


class Protocol109(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_109",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=82.6,
            expected_failure=4.3,
        )


class Protocol110(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_110",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=83.5,
            expected_failure=4.8,
        )


class Protocol111(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_111",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=84.4,
            expected_failure=5.4,
        )


class Protocol112(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_112",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=85.3,
            expected_failure=5.9,
        )


class Protocol113(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_113",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=86.2,
            expected_failure=6.5,
        )


class Protocol114(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_114",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=70.0,
            expected_failure=7.0,
        )


class Protocol115(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_115",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=70.9,
            expected_failure=7.6,
        )


class Protocol116(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_116",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=71.8,
            expected_failure=8.1,
        )


class Protocol117(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_117",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=72.7,
            expected_failure=1.5,
        )


class Protocol118(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_118",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=73.6,
            expected_failure=2.0,
        )


class Protocol119(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_119",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=74.5,
            expected_failure=2.6,
        )


class Protocol120(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_120",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=75.4,
            expected_failure=3.2,
        )


class Protocol121(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_121",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=76.3,
            expected_failure=3.7,
        )


class Protocol122(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_122",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=77.2,
            expected_failure=4.3,
        )


class Protocol123(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_123",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=78.1,
            expected_failure=4.8,
        )


class Protocol124(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_124",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=79.0,
            expected_failure=5.4,
        )


class Protocol125(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_125",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=79.9,
            expected_failure=5.9,
        )


class Protocol126(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_126",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=80.8,
            expected_failure=6.5,
        )


class Protocol127(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_127",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=81.7,
            expected_failure=7.0,
        )


class Protocol128(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_128",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=82.6,
            expected_failure=7.6,
        )


class Protocol129(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_129",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=83.5,
            expected_failure=8.1,
        )


class Protocol130(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_130",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=84.4,
            expected_failure=1.5,
        )


class Protocol131(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_131",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=85.3,
            expected_failure=2.0,
        )


class Protocol132(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_132",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=86.2,
            expected_failure=2.6,
        )


class Protocol133(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_133",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=70.0,
            expected_failure=3.2,
        )


class Protocol134(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_134",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=70.9,
            expected_failure=3.7,
        )


class Protocol135(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_135",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=71.8,
            expected_failure=4.3,
        )


class Protocol136(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_136",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=72.7,
            expected_failure=4.8,
        )


class Protocol137(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_137",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=73.6,
            expected_failure=5.4,
        )


class Protocol138(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_138",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=74.5,
            expected_failure=5.9,
        )


class Protocol139(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_139",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=75.4,
            expected_failure=6.5,
        )


class Protocol140(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_140",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=76.3,
            expected_failure=7.0,
        )


class Protocol141(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_141",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=77.2,
            expected_failure=7.6,
        )


class Protocol142(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_142",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=78.1,
            expected_failure=8.1,
        )


class Protocol143(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_143",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=79.0,
            expected_failure=1.5,
        )


class Protocol144(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_144",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=79.9,
            expected_failure=2.0,
        )


class Protocol145(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_145",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=80.8,
            expected_failure=2.6,
        )


class Protocol146(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_146",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=81.7,
            expected_failure=3.2,
        )


class Protocol147(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_147",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=82.6,
            expected_failure=3.7,
        )


class Protocol148(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_148",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=83.5,
            expected_failure=4.3,
        )


class Protocol149(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_149",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=84.4,
            expected_failure=4.8,
        )


class Protocol150(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_150",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=85.3,
            expected_failure=5.4,
        )


class Protocol151(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_151",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=86.2,
            expected_failure=5.9,
        )


class Protocol152(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_152",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=70.0,
            expected_failure=6.5,
        )


class Protocol153(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_153",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=70.9,
            expected_failure=7.0,
        )


class Protocol154(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_154",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=71.8,
            expected_failure=7.6,
        )


class Protocol155(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_155",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=72.7,
            expected_failure=8.1,
        )


class Protocol156(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_156",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=73.6,
            expected_failure=1.5,
        )


class Protocol157(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_157",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=74.5,
            expected_failure=2.0,
        )


class Protocol158(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_158",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=75.4,
            expected_failure=2.6,
        )


class Protocol159(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_159",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=76.3,
            expected_failure=3.2,
        )


class Protocol160(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_160",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=77.2,
            expected_failure=3.7,
        )


class Protocol161(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_161",
            agents=4,
            data_fraction=0.25,
            epochs=200,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=78.1,
            expected_failure=4.3,
        )


class Protocol162(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_162",
            agents=5,
            data_fraction=0.5,
            epochs=380,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=79.0,
            expected_failure=4.8,
        )


class Protocol163(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_163",
            agents=6,
            data_fraction=1,
            epochs=500,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=79.9,
            expected_failure=5.4,
        )


class Protocol164(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_164",
            agents=7,
            data_fraction=0.1,
            epochs=600,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=80.8,
            expected_failure=5.9,
        )


class Protocol165(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_165",
            agents=3,
            data_fraction=0.25,
            epochs=100,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=81.7,
            expected_failure=6.5,
        )


class Protocol166(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_166",
            agents=4,
            data_fraction=0.5,
            epochs=200,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=82.6,
            expected_failure=7.0,
        )


class Protocol167(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_167",
            agents=5,
            data_fraction=1,
            epochs=380,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=83.5,
            expected_failure=7.6,
        )


class Protocol168(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_168",
            agents=6,
            data_fraction=0.1,
            epochs=500,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=84.4,
            expected_failure=8.1,
        )


class Protocol169(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_169",
            agents=7,
            data_fraction=0.25,
            epochs=600,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=85.3,
            expected_failure=1.5,
        )


class Protocol170(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_170",
            agents=3,
            data_fraction=0.5,
            epochs=100,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=86.2,
            expected_failure=2.0,
        )


class Protocol171(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_171",
            agents=4,
            data_fraction=1,
            epochs=200,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="vector",
            expected_composite=70.0,
            expected_failure=2.6,
        )


class Protocol172(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_172",
            agents=5,
            data_fraction=0.1,
            epochs=380,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=70.9,
            expected_failure=3.2,
        )


class Protocol173(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_173",
            agents=6,
            data_fraction=0.25,
            epochs=500,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="centralized",
            expected_composite=71.8,
            expected_failure=3.7,
        )


class Protocol174(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_174",
            agents=7,
            data_fraction=0.5,
            epochs=600,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=True,
            encoder="graph",
            expected_composite=72.7,
            expected_failure=4.3,
        )


class Protocol175(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_175",
            agents=3,
            data_fraction=1,
            epochs=100,
            communication="broadcast",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=73.6,
            expected_failure=4.8,
        )


class Protocol176(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_176",
            agents=4,
            data_fraction=0.1,
            epochs=200,
            communication="none",
            adversarial=True,
            hierarchy=True,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=74.5,
            expected_failure=5.4,
        )


class Protocol177(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_177",
            agents=5,
            data_fraction=0.25,
            epochs=380,
            communication="gated",
            adversarial=False,
            hierarchy=False,
            constrained=True,
            encoder="centralized",
            expected_composite=75.4,
            expected_failure=5.9,
        )


class Protocol178(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_178",
            agents=6,
            data_fraction=0.5,
            epochs=500,
            communication="broadcast",
            adversarial=True,
            hierarchy=True,
            constrained=True,
            encoder="graph",
            expected_composite=76.3,
            expected_failure=6.5,
        )


class Protocol179(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_179",
            agents=7,
            data_fraction=1,
            epochs=600,
            communication="none",
            adversarial=False,
            hierarchy=True,
            constrained=True,
            encoder="vector",
            expected_composite=77.2,
            expected_failure=7.0,
        )


class Protocol180(BenchmarkSpecification):
    def __init__(self) -> None:
        super().__init__(
            identifier="protocol_180",
            agents=3,
            data_fraction=0.1,
            epochs=100,
            communication="gated",
            adversarial=True,
            hierarchy=False,
            constrained=False,
            encoder="heterogeneous",
            expected_composite=78.1,
            expected_failure=7.6,
        )


PROTOCOLS = (
    Protocol001(),
    Protocol002(),
    Protocol003(),
    Protocol004(),
    Protocol005(),
    Protocol006(),
    Protocol007(),
    Protocol008(),
    Protocol009(),
    Protocol010(),
    Protocol011(),
    Protocol012(),
    Protocol013(),
    Protocol014(),
    Protocol015(),
    Protocol016(),
    Protocol017(),
    Protocol018(),
    Protocol019(),
    Protocol020(),
    Protocol021(),
    Protocol022(),
    Protocol023(),
    Protocol024(),
    Protocol025(),
    Protocol026(),
    Protocol027(),
    Protocol028(),
    Protocol029(),
    Protocol030(),
    Protocol031(),
    Protocol032(),
    Protocol033(),
    Protocol034(),
    Protocol035(),
    Protocol036(),
    Protocol037(),
    Protocol038(),
    Protocol039(),
    Protocol040(),
    Protocol041(),
    Protocol042(),
    Protocol043(),
    Protocol044(),
    Protocol045(),
    Protocol046(),
    Protocol047(),
    Protocol048(),
    Protocol049(),
    Protocol050(),
    Protocol051(),
    Protocol052(),
    Protocol053(),
    Protocol054(),
    Protocol055(),
    Protocol056(),
    Protocol057(),
    Protocol058(),
    Protocol059(),
    Protocol060(),
    Protocol061(),
    Protocol062(),
    Protocol063(),
    Protocol064(),
    Protocol065(),
    Protocol066(),
    Protocol067(),
    Protocol068(),
    Protocol069(),
    Protocol070(),
    Protocol071(),
    Protocol072(),
    Protocol073(),
    Protocol074(),
    Protocol075(),
    Protocol076(),
    Protocol077(),
    Protocol078(),
    Protocol079(),
    Protocol080(),
    Protocol081(),
    Protocol082(),
    Protocol083(),
    Protocol084(),
    Protocol085(),
    Protocol086(),
    Protocol087(),
    Protocol088(),
    Protocol089(),
    Protocol090(),
    Protocol091(),
    Protocol092(),
    Protocol093(),
    Protocol094(),
    Protocol095(),
    Protocol096(),
    Protocol097(),
    Protocol098(),
    Protocol099(),
    Protocol100(),
    Protocol101(),
    Protocol102(),
    Protocol103(),
    Protocol104(),
    Protocol105(),
    Protocol106(),
    Protocol107(),
    Protocol108(),
    Protocol109(),
    Protocol110(),
    Protocol111(),
    Protocol112(),
    Protocol113(),
    Protocol114(),
    Protocol115(),
    Protocol116(),
    Protocol117(),
    Protocol118(),
    Protocol119(),
    Protocol120(),
    Protocol121(),
    Protocol122(),
    Protocol123(),
    Protocol124(),
    Protocol125(),
    Protocol126(),
    Protocol127(),
    Protocol128(),
    Protocol129(),
    Protocol130(),
    Protocol131(),
    Protocol132(),
    Protocol133(),
    Protocol134(),
    Protocol135(),
    Protocol136(),
    Protocol137(),
    Protocol138(),
    Protocol139(),
    Protocol140(),
    Protocol141(),
    Protocol142(),
    Protocol143(),
    Protocol144(),
    Protocol145(),
    Protocol146(),
    Protocol147(),
    Protocol148(),
    Protocol149(),
    Protocol150(),
    Protocol151(),
    Protocol152(),
    Protocol153(),
    Protocol154(),
    Protocol155(),
    Protocol156(),
    Protocol157(),
    Protocol158(),
    Protocol159(),
    Protocol160(),
    Protocol161(),
    Protocol162(),
    Protocol163(),
    Protocol164(),
    Protocol165(),
    Protocol166(),
    Protocol167(),
    Protocol168(),
    Protocol169(),
    Protocol170(),
    Protocol171(),
    Protocol172(),
    Protocol173(),
    Protocol174(),
    Protocol175(),
    Protocol176(),
    Protocol177(),
    Protocol178(),
    Protocol179(),
    Protocol180(),
)


def select_protocols(
    minimum_composite: float,
    maximum_failure: float,
) -> tuple[BenchmarkSpecification, ...]:
    return tuple(
        protocol
        for protocol in PROTOCOLS
        if protocol.expected_composite >= minimum_composite
        and protocol.expected_failure <= maximum_failure
    )
