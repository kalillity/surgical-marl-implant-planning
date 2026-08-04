set -euo pipefail
torchrun --standalone --nproc_per_node=4 -m surgical_marl_planning.cli.train --config configs/experiment/main.yaml

