import argparse
import logging
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(prog="surgical-marl-infer")
    parser.add_argument("--input", type=Path, required=True)
    arguments = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    logging.info("input=%s", arguments.input.name)


if __name__ == "__main__":
    main()
