"""Shared Anthropic client setup and cost accounting.

Both tools go through this module so that every call reports what it cost.
"""

import os
from dataclasses import dataclass

import anthropic
from dotenv import load_dotenv

DEFAULT_MODEL = "claude-sonnet-5-5"


@dataclass(frozen=True)
class Price:
    """USD per million tokens."""

    input: float
    output: float
    cache_read: float

    @property
    def cache_write(self) -> float:
        # 5-minute TTL cache writes cost 1.25x the base input price.
        return self.input * 1.25


# Prices checked 2026-10. Update here if Anthropic changes them.
PRICES: dict[str, Price] = {
    "claude-sonnet-5-5": Price(input=2.00, output=10.00, cache_read=0.20),
    "claude-opus-5-5": Price(input=4.00, output=20.00, cache_read=0.20),
}

EFFORTS = ("low", "medium", "high")


def has_api_key() -> bool:
    """Load .env (if present) and report whether an API key is configured."""
    load_dotenv()
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


def make_client() -> anthropic.Anthropic:
    """Build a client from ANTHROPIC_API_KEY (read from .env if present)."""
    load_dotenv()
    return anthropic.Anthropic()


def cost_usd(model: str, usage) -> float:
    """Cost of one response, from its `usage` block.

    `input_tokens` counts only the uncached part of the prompt; cached
    tokens are reported separately and billed at their own rates.
    Thinking tokens are included in `output_tokens`.
    """
    p = PRICES[model]
    per_token = (
        usage.input_tokens * p.input
        + (usage.cache_creation_input_tokens or 0) * p.cache_write
        + (usage.cache_read_input_tokens or 0) * p.cache_read
        + usage.output_tokens * p.output
    )
    return per_token / 1_000_000
