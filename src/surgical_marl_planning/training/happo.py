import math
from collections.abc import Iterable
from dataclasses import dataclass
from typing import cast

import torch
from torch import Tensor, nn

from surgical_marl_planning.losses.objectives import ClippedPolicyObjective, ClippedValueObjective


class GaussianPolicy(nn.Module):
    def __init__(self, input_dim: int = 256, action_dim: int = 8) -> None:
        super().__init__()
        self.mean = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.Tanh(),
            nn.Linear(256, action_dim),
        )
        self.log_standard_deviation = nn.Parameter(torch.full((action_dim,), -0.5))

    def distribution(self, state: Tensor) -> torch.distributions.Normal:
        mean = self.mean(state)
        deviation = self.log_standard_deviation.exp().expand_as(mean)
        return torch.distributions.Normal(mean, deviation)

    def forward(self, state: Tensor, deterministic: bool = False) -> tuple[Tensor, Tensor, Tensor]:
        mean = self.mean(state)
        deviation = self.log_standard_deviation.exp().expand_as(mean)
        action = mean if deterministic else mean + deviation * torch.randn_like(mean)
        log_probability, entropy = self.evaluate(state, action)
        return action, log_probability, entropy

    def evaluate(self, state: Tensor, action: Tensor) -> tuple[Tensor, Tensor]:
        mean = self.mean(state)
        log_deviation = self.log_standard_deviation.expand_as(mean)
        deviation = log_deviation.exp()
        normalized = (action - mean) / deviation
        constant = 0.5 * math.log(2 * math.pi)
        log_probability = (-0.5 * normalized.square() - log_deviation - constant).sum(-1)
        entropy = (log_deviation + 0.5 * math.log(2 * math.pi * math.e)).sum(-1)
        return log_probability, entropy


class CentralizedCritic(nn.Module):
    def __init__(self, latent_dim: int = 256, agents: int = 5) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(latent_dim * agents, 1024),
            nn.GELU(),
            nn.Linear(1024, 512),
            nn.GELU(),
            nn.Linear(512, 1),
        )

    def forward(self, states: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]) -> Tensor:
        return cast(Tensor, self.network(torch.cat(states, dim=-1)).squeeze(-1))


@dataclass(frozen=True)
class PolicyBatch:
    states: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    actions: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    old_log_probabilities: tuple[Tensor, Tensor, Tensor, Tensor, Tensor]
    advantages: Tensor
    returns: Tensor
    old_values: Tensor


class HAPPOUpdater:
    def __init__(
        self,
        policies: Iterable[GaussianPolicy],
        critic: CentralizedCritic,
        actor_learning_rate: float = 3e-4,
        critic_learning_rate: float = 1e-3,
    ) -> None:
        self.policies = list(policies)
        self.critic = critic
        self.actor_optimizers = [
            torch.optim.AdamW(policy.parameters(), lr=actor_learning_rate)
            for policy in self.policies
        ]
        self.critic_optimizer = torch.optim.AdamW(critic.parameters(), lr=critic_learning_rate)
        self.policy_objective = ClippedPolicyObjective()
        self.value_objective = ClippedValueObjective()

    def update(self, batch: PolicyBatch) -> dict[str, float]:
        factor = torch.ones_like(batch.advantages)
        losses: dict[str, float] = {}
        for index, (policy, optimizer) in enumerate(
            zip(self.policies, self.actor_optimizers, strict=True)
        ):
            new_log_probability, entropy = policy.evaluate(
                batch.states[index], batch.actions[index]
            )
            objective = self.policy_objective(
                new_log_probability,
                batch.old_log_probabilities[index],
                batch.advantages * factor,
                entropy,
            )
            optimizer.zero_grad(set_to_none=True)
            objective.backward()
            nn.utils.clip_grad_norm_(policy.parameters(), 0.5)
            optimizer.step()
            with torch.no_grad():
                factor = factor * torch.exp(
                    new_log_probability - batch.old_log_probabilities[index]
                )
            losses[f"actor_{index}"] = float(objective.detach())
        value = self.critic(batch.states)
        value_loss = self.value_objective(value, batch.old_values, batch.returns)
        self.critic_optimizer.zero_grad(set_to_none=True)
        value_loss.backward()
        nn.utils.clip_grad_norm_(self.critic.parameters(), 0.5)
        self.critic_optimizer.step()
        losses["critic"] = float(value_loss.detach())
        return losses
