import argparse
import logging
from pathlib import Path

import torch
import yaml

from surgical_marl_planning.randomness import set_seed
from surgical_marl_planning.system import SurgicalPlanningSystem


def main() -> None:
    parser = argparse.ArgumentParser(prog="surgical-marl-train")
    parser.add_argument("--config", type=Path, required=True)
    arguments = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    config = yaml.safe_load(arguments.config.read_text(encoding="utf-8"))
    set_seed(int(config["seed"]))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SurgicalPlanningSystem().to(device)
    parameters = sum(parameter.numel() for parameter in model.parameters())
    logging.info("model_parameters=%d device=%s", parameters, device)


if __name__ == "__main__":
    main()
