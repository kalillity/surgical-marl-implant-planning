import torch
from torch import Tensor, nn

TOPOLOGY = (
    (False, True, False, True, False),
    (False, False, True, True, True),
    (False, True, False, False, False),
    (False, True, False, False, True),
    (True, True, True, True, False),
)


class GatedCrossAttention(nn.Module):
    def __init__(self, latent_dim: int = 256, heads: int = 4, temperature: float = 0.5) -> None:
        super().__init__()
        if latent_dim % heads != 0:
            raise ValueError("latent_dim must be divisible by heads")
        self.latent_dim = latent_dim
        self.heads = heads
        self.head_dim = latent_dim // heads
        self.temperature = temperature
        self.query = nn.ModuleList(nn.Linear(latent_dim, latent_dim) for _ in range(5))
        self.key = nn.ModuleList(nn.Linear(latent_dim, latent_dim) for _ in range(5))
        self.value = nn.ModuleList(nn.Linear(latent_dim, latent_dim) for _ in range(5))
        self.gate = nn.ModuleDict(
            {
                f"{source}_{target}": nn.Linear(latent_dim * 2, heads)
                for source in range(5)
                for target in range(5)
                if TOPOLOGY[source][target]
            }
        )
        self.output = nn.ModuleList(nn.Linear(latent_dim, latent_dim) for _ in range(5))
        self.norm = nn.ModuleList(nn.LayerNorm(latent_dim) for _ in range(5))

    def forward(
        self, states: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    ) -> tuple[tuple[Tensor, Tensor, Tensor, Tensor, Tensor], Tensor, Tensor]:
        queries = [
            self.query[index](state).view(state.shape[0], self.heads, self.head_dim)
            for index, state in enumerate(states)
        ]
        keys = [
            self.key[index](state).view(state.shape[0], self.heads, self.head_dim)
            for index, state in enumerate(states)
        ]
        values = [
            self.value[index](state).view(state.shape[0], self.heads, self.head_dim)
            for index, state in enumerate(states)
        ]
        batch = states[0].shape[0]
        gates = states[0].new_zeros(batch, 5, 5, self.heads)
        attention = states[0].new_zeros(batch, 5, 5, self.heads)
        messages = [torch.zeros_like(values[index]) for index in range(5)]
        for source in range(5):
            for target in range(5):
                if not TOPOLOGY[source][target]:
                    continue
                score = (queries[target] * keys[source]).sum(-1) / self.head_dim**0.5
                weight = torch.softmax(score / self.temperature, dim=-1)
                gate = torch.sigmoid(
                    self.gate[f"{source}_{target}"](
                        torch.cat((states[target], states[source]), dim=-1)
                    )
                )
                gates[:, source, target] = gate
                attention[:, source, target] = weight
                messages[target] = (
                    messages[target] + gate.unsqueeze(-1) * weight.unsqueeze(-1) * values[source]
                )
        updated = tuple(
            self.norm[index](
                states[index] + self.output[index](messages[index].flatten(start_dim=1))
            )
            for index in range(5)
        )
        return (updated[0], updated[1], updated[2], updated[3], updated[4]), gates, attention
