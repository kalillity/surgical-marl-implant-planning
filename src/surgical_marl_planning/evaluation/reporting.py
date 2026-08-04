import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class EvaluationRecord:
    dataset: str
    composite: float
    trajectory_deviation_mm: float
    angular_error_deg: float
    dice: float
    collision_percent: float
    failure_percent: float


def write_records(path: Path, records: list[EvaluationRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(
        json.dumps([asdict(record) for record in records], indent=2),
        encoding="utf-8",
    )
    temporary.replace(path)
