"""
Solve the problem with string manipulation.
"""

from __future__ import annotations

from functools import partial

MAX_BITS = 32


def ceil_div(x: int, a: int):
    """Equivalent to ceil(x / a)"""
    return (x + a - 1) // a


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
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = map(partial(swap_k_groups_str, k=k), arr)

    print(" ".join(map(str, res)))
