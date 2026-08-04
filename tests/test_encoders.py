import torch

from surgical_marl_planning.models.encoders import (
    BiomechanicalEncoder,
    SegmentationEncoder,
    VectorEncoder,
    VerifierEncoder,
)


def test_segmentation_encoder_shapes() -> None:
    module = SegmentationEncoder(32, channels=(8, 16))
    latent, mask, uncertainty = module(torch.randn(2, 1, 16, 16, 16))
    assert latent.shape == (2, 32)
    assert mask.shape == (2, 1, 4, 4, 4)
    assert uncertainty.shape == mask.shape


def test_biomechanical_encoder_shapes() -> None:
    module = BiomechanicalEncoder(8, 32, 32, 2, 4)
    nodes = torch.randn(8, 8)
    edges = torch.tensor([[0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 0, 5, 6, 7]])
    batches = torch.tensor([0, 0, 0, 0, 1, 1, 1, 1])
    latent, stress = module(nodes, edges, batches)
    assert latent.shape == (2, 32)
    assert stress.shape == (8, 1)
    assert torch.all(stress > 0)


def test_vector_encoder_shape() -> None:
    module = VectorEncoder(12, 32, 64, 4)
    assert module(torch.randn(3, 12)).shape == (3, 32)


def test_verifier_encoder_shapes() -> None:
    module = VerifierEncoder(32, 4, 2)
    latent, decision, failure = module(torch.randn(2, 5, 32))
    assert latent.shape == (2, 32)
    assert decision.shape == (2, 3)
    assert failure.shape == (2, 4)
