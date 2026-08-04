# Multi-agent reinforcement learning for patient-specific implant planning

This repository contains the training and evaluation implementation for adversarial-cooperative surgical planning with five specialized agents. The system combines volumetric segmentation, graph-based biomechanical stress prediction, parametric implant design, trajectory planning, and iterative verification through gated cross-attention under centralized training and decentralized execution.

## Installation

Python 3.11 and CUDA 12.4 are the supported environment.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

The Conda environment is created with `conda env create -f environment.yml`. The container is built with `docker build -t surgical-marl-planning .`.

## Data

Canonical dataset locations and licenses are listed in `dataset_links.txt`. The training corpus consists of CTPelvic1K 1.0, VerSe 2020, TotalSegmentator v2.0, CTSpine1K 1.0, and PENGWIN 2024. Volumes are resampled to 1 mm isotropic spacing, clipped to the bone window from -200 to 1500 HU, normalized to the unit interval, cropped to the anatomical region with a 20 mm margin, and split 80:20 by source and pathology. A 118-case CTPelvic1K validation subset is reserved from the training partition.

## Training

The reported experiment uses 4 NVIDIA A100 80GB GPUs, 2048 transitions per batch, 500 epochs, five million environment steps, and five independent seeds.

```bash
torchrun --standalone --nproc_per_node=4 -m surgical_marl_planning.cli.train --config configs/experiment/main.yaml
```

The actor learning rate is 3e-4 and the critic learning rate is 1e-3. Both use a 5% linear warm-up followed by cosine decay. Cooperative training occupies 60% of the schedule. Adversarial verification ramps linearly during the remaining stage. The FEA surrogate is trained separately for 200 epochs on 24,000 meshes.

Each configuration in `configs/experiment` corresponds to the main experiment or one of ten architectural and training ablations.

## Evaluation

```bash
python -m surgical_marl_planning.cli.evaluate --weights artifacts/model.pt
```

The pooled five-seed targets are composite quality 87.3 ± 1.2, trajectory deviation 1.52 ± 0.18 mm, angular error 2.34 ± 0.24 degrees, Dice 0.946 ± 0.010, collision rate 2.1 ± 0.6%, and failure rate 2.1 ± 0.5%. FEA surrogate targets are R² 0.947 ± 0.008 and MAE 0.042 ± 0.006 MPa.

Generalization gaps are evaluated across dataset, anatomical site, pathology, and demographic axes with thresholds of 8%, 12%, 15%, and 10%, respectively. Bootstrap intervals, paired standardized effects, MCID crossing rates, subgroup gaps, communication gate activations, scaling behavior, and per-dataset results are available through the evaluation modules.

## Compute budget

The full three-stage protocol requires approximately 72 hours on 4 NVIDIA A100 80GB GPUs. FEA generation uses 24,000 tetrahedral simulations and the final training loop performs approximately 2.4 million surrogate evaluations. Local storage needs depend on retained source DICOM/NIfTI volumes, meshes, and FEA fields; provision at least 2 TB when retaining all intermediate meshes and solver outputs.

## Verification

```bash
pytest -q
ruff check .
mypy --strict src/surgical_marl_planning
```

The suite covers preprocessing, encoder shapes, graph attention, communication topology, constrained rewards, schedule transitions, clinical metrics, statistics, configuration regression, and integrated policy updates.

## License

The software is distributed under the MIT License. Dataset licenses remain governed by their respective sources.

