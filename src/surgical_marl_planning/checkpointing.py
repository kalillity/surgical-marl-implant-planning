import os
from pathlib import Path
from typing import Any

import torch
from torch import nn


def save_checkpoint(
    path: Path,
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    seed: int,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    payload: dict[str, Any] = {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "epoch": epoch,
        "seed": seed,
        "rng": torch.get_rng_state(),
    }
    torch.save(payload, temporary)
    os.replace(temporary, path)


def load_checkpoint(
    path: Path, model: nn.Module, optimizer: torch.optim.Optimizer
) -> tuple[int, int]:
    payload = torch.load(path, map_location="cpu", weights_only=False)
    model.load_state_dict(payload["model"])
    optimizer.load_state_dict(payload["optimizer"])
    torch.set_rng_state(payload["rng"])
    return int(payload["epoch"]), int(payload["seed"])
