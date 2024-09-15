"""The solution to the quiz problem.
Used for generating the test cases.
The `ac_code.py` do not import this module for isolation.
"""

from __future__ import annotations

import random
from functools import reduce

MAX_BITS = 32


def ceil_div(x: int, a: int):
    """Equivalent to ceil(x / a)"""
    return (x + a - 1) // a


def swap_k_groups(x: int, k: int) -> int:
    assert 0 <= x < 2**MAX_BITS and 0 <= k <= MAX_BITS
    if k == 0:
        return x

    overflow_mask = (1 << 32) - 1

    mask_unit = (1 << k) - 1  # consecutive k bits

    mask_low = reduce(
        lambda x, y: x | y,
        [(mask_unit << 2 * i * k) & overflow_mask for i in range(ceil_div(MAX_BITS, (k * 2)))],
        0,
    )
    mask_high = reduce(
        lambda x, y: x | y,
        [
            # mask_unit << shift
            # for i in range(MAX_BITS // k)
            # if ((shift := (2 * i + 1) * k) + k - 1 < MAX_BITS)
            (mask_unit << (2 * i + 1) * k) & overflow_mask
            for i in range(ceil_div(MAX_BITS - k, (k * 2)))
        ],
        0,
    )

    # print(f"{mask_high:>032b}")
    # print(f"{mask_low:>032b}")
    assert mask_high & mask_low == 0 and mask_high | mask_low == overflow_mask

    # print(f"{(x & mask_high) >> k:>032b}")
    # print(f"{( x & mask_low ) << k:>032b}")

    res = ((x & mask_high) >> k) | ((x & mask_low) << k)
    return res & overflow_mask


def swap_k_groups_str(x: int, k: int) -> int:
    assert 0 <= x < 2**MAX_BITS and 0 <= k <= MAX_BITS
    if k == 0:
        return x
    if k == MAX_BITS:
        return 0

    x_bits = bin(x)[2:].zfill(MAX_BITS)

    x_low_revs = [x_bits[::-1][i : i + k].ljust(k, "0") for i in range(0, MAX_BITS, 2 * k)]
    x_high_revs = [x_bits[::-1][i : i + k].ljust(k, "0") for i in range(k, MAX_BITS, 2 * k)]

    # if x_low_revs is longer, then the extra group will be simply dropped by `zip`
    assert len(x_low_revs) >= len(x_high_revs)

    res = "".join("".join(pair) for pair in zip(x_high_revs, x_low_revs))

    return int(res[:MAX_BITS][::-1], 2)


if __name__ == "__main__":
    for _ in range(10000):
        x = random.randint(0, 2**MAX_BITS - 1)
        for k in range(32):
            ans1 = swap_k_groups(x, k)
            ans2 = swap_k_groups_str(x, k)
            assert ans1 == ans2, (x, k, ans1, ans2)
