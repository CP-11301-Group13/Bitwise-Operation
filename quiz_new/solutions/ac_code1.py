"""The solution to the quiz problem.
Used for generating the test cases.
The `ac_code.py` do not import this module for isolation.
"""

from __future__ import annotations

import random
from functools import partial, reduce

MAX_BITS = 32


def ceil_div(x: int, a: int):
    """Equivalent to ceil(x / a)"""
    return (x + a - 1) // a


def swap_k_groups(x: int, k: int) -> int:
    assert 0 <= x < 2**MAX_BITS and 0 <= k < MAX_BITS
    if k == 0:
        return x

    overflow_mask = (1 << 32) - 1

    mask_unit = (1 << k) - 1  # consecutive k bits

    mask_low = reduce(
        lambda x, y: x | y,
        [
            (mask_unit << 2 * i * k) & overflow_mask
            for i in range(ceil_div(MAX_BITS, (k * 2)))
        ],
    )
    mask_high = reduce(
        lambda x, y: x | y,
        [
            (mask_unit << (2 * i + 1) * k) & overflow_mask
            for i in range(ceil_div(MAX_BITS - k, (k * 2)))
        ],
    )

    assert mask_high & mask_low == 0 and mask_high | mask_low == overflow_mask

    res = ((x & mask_high) >> k) | ((x & mask_low) << k)
    return res & overflow_mask


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = map(partial(swap_k_groups, k=k), arr)

    print(" ".join(map(str, res)))
