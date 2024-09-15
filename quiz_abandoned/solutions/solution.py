"""The solution to the quiz problem.
Used for generating the test cases. Also used by `level[1-4].py`.
The `ac_code.py` consists of a copy of this file.
"""

from __future__ import annotations

import random
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


def calc_X_n_squared(numbers: list[int]) -> int:
    """Calculate X using the naive O(n^2) approach"""

    n = len(numbers)
    X = 0
    for i in range(n):
        for j in range(n):
            ai = get_odd_bits(numbers[i])
            bj = get_even_bits(numbers[j])
            X ^= ai & bj
    return X


def check_flip(numbers: list[int], x: int, flip_idx: int) -> bool:
    """Check if flipping the bit at flip_idx of x will reduce the value of X"""

    before = reduce(lambda a, b: a ^ b, [x & y & (1 << flip_idx) for y in numbers])

    x_flip = x ^ (1 << flip_idx)
    after = reduce(lambda a, b: a ^ b, [x_flip & y & (1 << flip_idx) for y in numbers])

    return after < before


def minimize_X_n_squared(numbers: list[int], k: int) -> tuple[int, list[int]]:
    numbers = numbers.copy()
    n = len(numbers)
    max_bit = max(numbers).bit_length()

    arr_a = [get_odd_bits(num) for num in numbers]
    arr_b = [get_odd_bits(num) for num in numbers]

    # Calculate initial X
    X = calc_X_n_squared(numbers)

    for _ in range(k):
        best_X = X
        best_flip = None

        # Starting from the most significant bit
        for pos in range(max_bit - 1, -1, -1):
            if best_flip:
                break

            for i in range(n):
                half_pos = pos // 2
                is_odd = pos % 2

                if not best_X & (1 << half_pos):
                    continue

                should_flip = (
                    check_flip(arr_b, arr_a[i], half_pos)
                    if is_odd
                    else check_flip(arr_a, arr_b[i], half_pos)
                )
                if should_flip:
                    best_X ^= 1 << half_pos
                    best_flip = (i, pos)

        if best_flip:
            i, pos = best_flip
            numbers[i] ^= 1 << pos
            X = best_X
        else:
            break  # No improvement possible

    return X, numbers


def calc_X(numbers: list[int]) -> int:
    """Calculate X using the optimal O(n) approach"""

    ais = [get_odd_bits(num) for num in numbers]
    bis = [get_even_bits(num) for num in numbers]

    a_xor = reduce(lambda x, y: x ^ y, ais)
    b_xor = reduce(lambda x, y: x ^ y, bis)

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
        # `ones_positions` is from left to right, so we need to flip from right to left
        # Note that the position has to be doubled
        numbers[0] ^= 1 << ((max_bit - pos - 1) * 2)

    new_X = calc_X(numbers)
    return new_X, numbers


if __name__ == "__main__":
    # Example usage
    cnt = 0
    for _ in range(10):
        numbers = [random.randint(1, 2**10) for _ in range(1000)]
        # fmt: off
        # numbers= [149, 497, 189, 205, 79, 346, 999, 225, 415, 188, 505, 780, 349, 181, 30, 133, 261, 955, 223, 971, 670, 898, 227, 375, 407, 916, 998, 791, 981, 154, 703, 1022, 857, 42, 730, 870, 118, 657, 225, 528, 115, 250, 384, 939, 524, 315, 528, 346, 850, 289, 150, 512, 967, 279, 807, 480, 626, 622, 746, 562, 115, 375, 505, 716, 784, 499, 120, 29, 685, 427, 361, 574, 795, 1006, 594, 761, 266, 748, 400, 967, 789, 715, 121, 577, 1015, 774, 413, 430, 779, 846, 762, 820, 940, 342, 200, 765, 675, 220, 982, 216, 583, 989, 252, 637, 938, 164, 657, 322, 457, 996, 553, 508, 153, 730, 174, 761, 773, 203, 413, 336, 982, 864, 179, 646, 337, 792, 629, 205, 899, 35, 612, 211, 823, 214, 198, 829, 4, 914, 701, 225, 387, 782, 272, 443, 907, 775, 271, 318, 363, 168, 440, 100, 602, 820, 338, 998, 809, 333, 769, 414, 1023, 564, 225, 153, 613, 938, 519, 611, 610, 679, 272, 798, 100, 611, 108, 315, 596, 906, 960, 394, 14, 334, 335, 650, 99, 881, 433, 650, 203, 817, 4, 101, 738, 211, 835, 730, 217, 344, 791, 710, 869, 926, 206, 207, 705, 543, 561, 484, 396, 705, 203, 4, 878, 411, 345, 526, 357, 17, 421, 502, 395, 528, 911, 240, 107, 560, 57, 210, 913, 806, 225, 4, 865, 841, 943, 742, 790, 203, 85, 497, 840, 814, 941, 821, 405, 110, 972, 986, 31, 72, 1020, 783, 57, 277, 992, 585, 600, 331, 639, 224, 245, 624, 111, 763, 468, 70, 252, 250, 988, 931, 367, 556, 467, 224, 960, 647, 994, 827, 995, 88, 657, 575, 933, 319, 575, 734, 323, 702, 732, 733, 35, 674, 543, 328, 406, 945, 630, 747, 288, 484, 639, 813, 644, 592, 760, 560, 278, 184, 504, 809, 272, 74, 602, 207, 582, 905, 730, 921, 104, 864, 913, 70, 1015, 784, 332, 241, 556, 645, 518, 739, 1007, 507, 777, 714, 2, 310, 395, 96, 345, 583, 649, 106, 325, 772, 700, 693, 412, 176, 592, 450, 644, 184, 625, 456, 341, 690, 561, 456, 263, 419, 222, 208, 532, 758, 929, 80, 307, 672, 648, 899, 346, 527, 621, 1020, 281, 41, 703, 260, 443, 247, 52, 920, 235, 325, 600, 177, 426, 788, 847, 362, 804, 827, 783, 188, 1006, 889, 700, 659, 1007, 115, 938, 599, 820, 51, 167, 447, 523, 143, 421, 26, 689, 172, 157, 236, 126, 973, 86, 993, 633, 837, 351, 610, 210, 863, 772, 420, 718, 82, 688, 542, 825, 876, 328, 503, 378, 323, 22, 818, 564, 847, 967, 506, 840, 691, 154, 283, 420, 171, 105, 665, 747, 963, 186, 125, 989, 773, 198, 98, 600, 761, 876, 980, 473, 513, 212, 149, 533, 523, 204, 497, 14, 377, 944, 950, 795, 500, 313, 173, 649, 134, 601, 756, 175, 258, 573, 435, 537, 934, 682, 559, 391, 874, 443, 266, 673, 18, 351, 487, 951, 800, 802, 224, 807, 7, 663, 760, 748, 302, 262, 512, 491, 276, 369, 330, 77, 28, 232, 584, 825, 208, 364, 834, 815, 28, 94, 385, 840, 408, 444, 839, 269, 221, 900, 358, 891, 719, 39, 336, 625, 981, 186, 978, 166, 519, 589, 997, 605, 624, 950, 344, 793, 487, 202, 735, 959, 593, 52, 208, 983, 738, 962, 312, 813, 277, 881, 344, 560, 475, 405, 351, 234, 251, 189, 503, 700, 741, 626, 244, 450, 381, 762, 835, 743, 355, 126, 296, 465, 142, 134, 307, 309, 953, 644, 573, 479, 164, 519, 56, 736, 35, 985, 922, 740, 895, 421, 455, 732, 928, 648, 437, 177, 360, 121, 165, 385, 926, 232, 174, 272, 747, 154, 974, 63, 1013, 577, 54, 234, 407, 126, 505, 474, 257, 258, 497, 837, 51, 195, 964, 11, 641, 322, 996, 623, 437, 224, 420, 65, 26, 300, 680, 572, 710, 562, 579, 622, 839, 835, 278, 946, 915, 540, 954, 465, 209, 627, 1002, 853, 75, 873, 757, 337, 721, 885, 525, 756, 78, 256, 655, 485, 383, 461, 424, 651, 716, 830, 789, 357, 429, 579, 367, 196, 771, 899, 667, 1014, 789, 890, 897, 105, 686, 752, 281, 88, 56, 572, 384, 862, 860, 253, 547, 387, 948, 486, 178, 479, 565, 2, 346, 853, 487, 855, 983, 936, 849, 307, 881, 405, 580, 338, 255, 301, 890, 749, 820, 734, 357, 836, 783, 123, 754, 844, 27, 233, 15, 682, 151, 73, 911, 478, 974, 854, 636, 742, 602, 251, 914, 956, 848, 207, 214, 88, 43, 658, 829, 139, 397, 215, 346, 78, 847, 480, 756, 421, 1006, 976, 229, 625, 59, 559, 785, 793, 337, 391, 514, 615, 741, 326, 921, 733, 632, 199, 1000, 527, 948, 912, 490, 952, 904, 693, 407, 543, 361, 322, 945, 4, 189, 387, 937, 384, 933, 765, 383, 916, 577, 935, 109, 535, 968, 249, 37, 557, 965, 293, 771, 733, 607, 414, 126, 616, 322, 440, 527, 78, 319, 711, 1007, 798, 411, 559, 752, 919, 202, 10, 142, 197, 838, 286, 896, 128, 1002, 582, 949, 885, 263, 292, 641, 691, 592, 692, 334, 358, 134, 713, 856, 781, 462, 524, 605, 392, 596, 440, 864, 164, 485, 606, 766, 53, 624, 853, 772, 917, 981, 840, 205, 658, 108, 230, 566, 866, 423, 274, 214, 444, 431, 964, 96, 416, 1016, 478, 873, 167, 548, 897, 68, 352, 258, 726, 432, 422, 831, 218, 760, 605, 762, 321, 849, 46, 908, 272, 864, 776, 961, 496, 559, 1024, 649, 558, 475, 714, 337, 849, 597, 844, 452, 686, 618, 627, 178, 549, 883, 523, 92, 556, 659, 853, 505, 337, 68, 144, 518, 392, 626, 591, 782, 481, 111, 182, 573, 977, 500, 583, 899, 604, 837, 1017, 944, 33, 971, 495, 315, 173, 819, 87, 644, 696, 204, 820, 540, 97, 16, 952, 920, 930, 984, 184, 622, 1001, 902, 748, 48, 20, 86, 189, 542, 716, 928, 313, 457, 959, 764]
        # fmt: on
        k = random.randint(1, 5)
        k = 1

        original_X = calc_X(numbers)
        minimized_X, new_numbers = minimize_X(numbers.copy(), k)
        minimized_X2, new_numbers = minimize_X_n_squared(numbers.copy(), k)

        print(f"Original X: {original_X:08b}")
        print(f"Minimized X: {minimized_X:08b}")
        print(f"Minimized X2: {minimized_X2:08b}")

        # assert minimized_X == minimized_X2, numbers
        assert minimized_X == minimized_X2

        # print(f"Original numbers: {numbers}")
        # print(f"k: {k}")
        # print(f"New numbers: {new_numbers}")
        # print()

        cnt += original_X > 0

        assert minimized_X2 <= original_X
        # print(comp)
        # break
    # print(cnt)
