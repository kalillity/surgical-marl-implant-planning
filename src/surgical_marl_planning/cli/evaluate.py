import argparse
import logging
from pathlib import Path

import torch

from surgical_marl_planning.system import SurgicalPlanningSystem


def main() -> None:
    parser = argparse.ArgumentParser(prog="surgical-marl-evaluate")
    parser.add_argument("--weights", type=Path, required=True)
    arguments = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    model = SurgicalPlanningSystem()
    state = torch.load(arguments.weights, map_location="cpu", weights_only=True)
    model.load_state_dict(state)
    model.eval()
    logging.info("weights_loaded=%s", arguments.weights.name)


if __name__ == "__main__":
    main()
