from collections.abc import Sequence
from typing import cast

import torch
from torch import Tensor, nn
from torch.nn import functional as functional


class ResidualVolumeBlock(nn.Module):
    def __init__(self, channels: int) -> None:
        super().__init__()
        self.depthwise = nn.Conv3d(channels, channels, 3, padding=1, groups=channels)
        self.norm = nn.GroupNorm(8, channels)
        self.expand = nn.Conv3d(channels, channels * 4, 1)
        self.contract = nn.Conv3d(channels * 4, channels, 1)

    def forward(self, values: Tensor) -> Tensor:
        hidden = self.depthwise(values)
        hidden = self.norm(hidden)
        hidden = functional.gelu(self.expand(hidden))
        return cast(Tensor, values + self.contract(hidden))


class SegmentationEncoder(nn.Module):
    def __init__(self, latent_dim: int = 256, channels: Sequence[int] = (32, 64, 128, 256)) -> None:
        super().__init__()
        stages: list[nn.Module] = []
        previous = 1
        for channel in channels:
            stages.extend(
                [
                    nn.Conv3d(previous, channel, 3, stride=2, padding=1),
                    nn.GroupNorm(8, channel),
                    nn.GELU(),
                    ResidualVolumeBlock(channel),
                    ResidualVolumeBlock(channel),
                ]
            )
            previous = channel
        self.encoder = nn.Sequential(*stages)
        self.pool = nn.AdaptiveAvgPool3d(1)
        self.latent = nn.Linear(previous, latent_dim)
        self.mask_head = nn.Conv3d(previous, 1, 1)
        self.uncertainty_head = nn.Conv3d(previous, 1, 1)

    def forward(self, volume: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        features = self.encoder(volume)
        latent = self.latent(self.pool(features).flatten(1))
        mask = torch.sigmoid(self.mask_head(features))
        uncertainty = torch.sigmoid(self.uncertainty_head(features))
        return latent, mask, uncertainty


class GraphAttentionLayer(nn.Module):
    def __init__(self, input_dim: int, output_dim: int, heads: int = 4) -> None:
        super().__init__()
        if output_dim % heads != 0:
            raise ValueError("output_dim must be divisible by heads")
        self.heads = heads
        self.head_dim = output_dim // heads
        self.query = nn.Linear(input_dim, output_dim)
        self.key = nn.Linear(input_dim, output_dim)
        self.value = nn.Linear(input_dim, output_dim)
        self.output = nn.Linear(output_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.residual = (
            nn.Linear(input_dim, output_dim) if input_dim != output_dim else nn.Identity()
        )

    def forward(self, nodes: Tensor, edge_index: Tensor) -> Tensor:
        source, target = edge_index
        query = self.query(nodes).view(nodes.shape[0], self.heads, self.head_dim)
        key = self.key(nodes).view(nodes.shape[0], self.heads, self.head_dim)
        value = self.value(nodes).view(nodes.shape[0], self.heads, self.head_dim)
        scores = (query[target] * key[source]).sum(-1) / self.head_dim**0.5
        weights = torch.zeros_like(scores)
        for node in torch.unique(target):
            selected = target == node
            weights[selected] = torch.softmax(scores[selected], dim=0)
        messages = value[source] * weights.unsqueeze(-1)
        aggregate = torch.zeros_like(value)
        aggregate.index_add_(0, target, messages)
        update = self.output(aggregate.flatten(1))
        return cast(Tensor, self.norm(self.residual(nodes) + update))


class BiomechanicalEncoder(nn.Module):
    def __init__(
        self,
        node_dim: int = 8,
        hidden_dim: int = 256,
        latent_dim: int = 256,
        layers: int = 8,
        heads: int = 4,
    ) -> None:
        super().__init__()
        blocks = [GraphAttentionLayer(node_dim, hidden_dim, heads)]
        blocks.extend(GraphAttentionLayer(hidden_dim, hidden_dim, heads) for _ in range(layers - 1))
        self.blocks = nn.ModuleList(blocks)
        self.latent = nn.Linear(hidden_dim, latent_dim)
        self.stress = nn.Linear(hidden_dim, 1)

    def forward(
        self, nodes: Tensor, edge_index: Tensor, batch_index: Tensor
    ) -> tuple[Tensor, Tensor]:
        hidden = nodes
        for block in self.blocks:
            hidden = functional.gelu(block(hidden, edge_index))
        batch_count = int(batch_index.max().item()) + 1
        pooled = torch.zeros(
            batch_count, hidden.shape[-1], device=hidden.device, dtype=hidden.dtype
        )
        pooled.index_add_(0, batch_index, hidden)
        counts = torch.bincount(batch_index, minlength=batch_count).clamp_min(1).unsqueeze(-1)
        pooled = pooled / counts
        return self.latent(pooled), functional.softplus(self.stress(hidden))


class VectorEncoder(nn.Module):
    def __init__(
        self, input_dim: int, latent_dim: int = 256, hidden_dim: int = 512, layers: int = 6
    ) -> None:
        super().__init__()
        modules: list[nn.Module] = [nn.Linear(input_dim, hidden_dim), nn.GELU()]
        for _ in range(layers - 2):
            modules.extend([nn.Linear(hidden_dim, hidden_dim), nn.LayerNorm(hidden_dim), nn.GELU()])
        modules.append(nn.Linear(hidden_dim, latent_dim))
        self.network = nn.Sequential(*modules)

    def forward(self, values: Tensor) -> Tensor:
        return cast(Tensor, self.network(values))


class VerifierEncoder(nn.Module):
    def __init__(
        self, latent_dim: int = 256, heads: int = 4, layers: int = 4, failure_types: int = 4
    ) -> None:
        super().__init__()
        block = nn.TransformerEncoderLayer(
            latent_dim,
            heads,
            latent_dim * 4,
            batch_first=True,
            norm_first=True,
            activation="gelu",
        )
        self.transformer = nn.TransformerEncoder(block, layers)
        self.decision = nn.Linear(latent_dim, 3)
        self.failure = nn.Linear(latent_dim, failure_types)

    def forward(self, states: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        encoded = self.transformer(states)
        pooled = encoded.mean(1)
        return pooled, self.decision(pooled), self.failure(pooled)
