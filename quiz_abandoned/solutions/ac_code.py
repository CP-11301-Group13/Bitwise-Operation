from __future__ import annotations

from functools import reduce


def get_odd_bits(n: int) -> int:
    """Get the odd bits of a number n.
    E.g. n = 0b10110 -> 0b01 = 1
    """
    if n == 0 or n == 1:
        return 0
    return int("".join(reversed(bin(n)[2:][-2::-2])), 2)


def get_even_bits(n: int) -> int:
    """Get the even bits of a number n.
    E.g. n = 0b10110 -> 0b110 = 6
    """
    return int("".join(reversed(bin(n)[2:][-1::-2])), 2)


def calc_X(numbers: list[int]) -> int:
    """Calculate X using the optimal O(n) approach"""

    arr_a = [get_odd_bits(num) for num in numbers]
    arr_b = [get_even_bits(num) for num in numbers]

    a_xor = reduce(lambda x, y: x ^ y, arr_a)
    b_xor = reduce(lambda x, y: x ^ y, arr_b)

    return a_xor & b_xor


def minimize_X(numbers: list[int], k: int) -> tuple[int, list[int]]:
    numbers = numbers.copy()
    max_bit = max(numbers).bit_length()

    X = calc_X(numbers)

    # Find k most significant 1 bits in X
    X_bits = bin(X)[2:].zfill(max_bit)
    ones_positions = [i for i in range(max_bit) if X_bits[i] == "1"]
    flip_positions = sorted(ones_positions)[:k]

    for pos in flip_positions:
        # Note: `ones_positions` is from left to right, so we need to flip from right to left,
        # and the position has to be doubled
        numbers[0] ^= 1 << ((max_bit - pos - 1) * 2)

    new_X = calc_X(numbers)
    return new_X, numbers


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    assert len(arr) == n
    X = calc_X(arr)
    X_min, _ = minimize_X(arr, k)

    print(X, X_min)
