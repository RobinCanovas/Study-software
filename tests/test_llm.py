from types import SimpleNamespace

import pytest

from study.llm import PRICES, cost_usd


def usage(input=0, cache_write=0, cache_read=0, output=0):
    return SimpleNamespace(
        input_tokens=input,
        cache_creation_input_tokens=cache_write,
        cache_read_input_tokens=cache_read,
        output_tokens=output,
    )


def test_cost_uncached_sonnet():
    # 1M input at $2 + 1M output at $10
    assert cost_usd("claude-sonnet-5-5", usage(input=1_000_000, output=1_000_000)) == pytest.approx(12.0)


def test_cache_write_is_1_25x_input_and_read_is_cheap():
    p = PRICES["claude-sonnet-5-5"]
    assert cost_usd("claude-sonnet-5-5", usage(cache_write=1_000_000)) == pytest.approx(p.input * 1.25)
    assert cost_usd("claude-sonnet-5-5", usage(cache_read=1_000_000)) == pytest.approx(0.20)


def test_missing_cache_fields_count_as_zero():
    u = usage(input=1000, output=100)
    u.cache_creation_input_tokens = None
    u.cache_read_input_tokens = None
    assert cost_usd("claude-sonnet-5-5", u) == pytest.approx((1000 * 2 + 100 * 10) / 1e6)
