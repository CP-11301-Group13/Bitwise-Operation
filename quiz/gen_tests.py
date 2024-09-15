"""
The difficulty of testcase should be classified into 4 main levels:

1. (30%) k = 0, n <= 1e3
2. (30%) k = 0, n <= 1e5
3. (20%) 0 < k < 32, n <= 1e3
4. (20%) 0 < k < 32, n <= 1e5

For every levels, 0 <= x < 2^32

---

Format of `subtasks.py`:

[score, [input_file, output_file, time_limit, memory_limit, output_limit]]
"""

from __future__ import annotations

import json
import random
import shutil
from dataclasses import dataclass
from pathlib import Path
from time import time
from typing import Callable

from solutions.solution import (
    calc_X,
    calc_X_n_squared,
    minimize_X,
    minimize_X_n_squared,
)

# --------------------------------- Constants -------------------------------- #

random.seed("CP113-1 RANDOM SEED")

TIME_LIMIT = 2
MEMORY_LIMIT = 64 << 20
OUTPUT_LIMIT = 64 << 10


# ---------------------------------- Helpers --------------------------------- #


@dataclass
class Input:
    arr: list[int]
    k: int

    def format(self):
        n = len(self.arr)
        return f"{n} {self.k}\n" + " ".join(map(str, self.arr))


@dataclass
class Output:
    X: int
    X_min: int

    def format(self):
        return f"{self.X} {self.X_min}"


SubtaskFunc = Callable[[], tuple[Input, Output]]

score_map: dict[int, int] = {}
func_map: dict[int, Callable[[], bool]] = {}


TESTS_DIR = Path(__file__).parent / "tests"
SUBTASKS_FILE = Path(__file__).parent / "subtasks.py"


def subtask(*, idx: int, score: int):
    if idx in score_map:
        raise ValueError(f"Duplicate subtask {idx}")
    score_map[idx] = score

    def wrap(func: SubtaskFunc) -> Callable[[], bool]:
        def new_func():
            try:
                in_str, out_str = func()

                in_file = TESTS_DIR / f"{idx}.in"
                in_file.write_text(in_str.format())
                out_file = TESTS_DIR / f"{idx}.out"
                out_file.write_text(out_str.format())
                return True
            except TypeError:
                print(f"WARNING: Failed generating subtask {idx}")
                return False

        func_map[idx] = new_func
        return new_func

    return wrap


def gen_subtasks(*idxs: int):
    shutil.rmtree(TESTS_DIR, ignore_errors=True)
    TESTS_DIR.mkdir()

    subtask_suc = {}
    for idx, func in func_map.items():
        if idxs and idx not in idxs:
            continue

        st = time()
        subtask_suc[idx] = func()
        if time() - st > TIME_LIMIT:
            print(f"WARNING: Subtask {idx} is too slow")

    score_map_suc = {
        idx: score for idx, score in score_map.items() if subtask_suc.get(idx, False)
    }
    if set(score_map_suc.keys()) != set(range(max(len(score_map), max(score_map) + 1))):
        missing_ids = set(range(len(score_map))) - score_map_suc.keys()
        print(f"WARNING: Subtask ids are missing: {sorted(missing_ids)}")
    if sum(score_map_suc.values()) != 100:
        print(f"WANRING: Sum of scores is not 100: {sum(score_map_suc.values())}")

    with open(SUBTASKS_FILE, "+w") as f:
        subtasks_spec = [
            [score, [f"{idx}.in", f"{idx}.out", TIME_LIMIT, MEMORY_LIMIT, OUTPUT_LIMIT]]
            for idx, score in score_map.items()
            if subtask_suc.get(idx, False)
        ]
        # we should manual format the file
        json.dump(subtasks_spec, f)


# --------------------------------- Subtasks --------------------------------- #

# * Level 1: k = 0, n <= 1e3


@subtask(idx=0, score=10)
def test_example():
    k = 0
    arr = [3, 6, 2, 5, 9, 14]

    # use slow solution to ensure this can be passed with O(n^2)
    X = calc_X_n_squared(arr)

    return Input(arr, k), Output(X, X)


@subtask(idx=1, score=10)
def test_1():
    n = random.randint(100, 1000)
    k = 0
    arr = [random.randint(0, 2**32) for _ in range(n)]

    X = calc_X_n_squared(arr)

    return Input(arr, k), Output(X, X)


# TODO
@subtask(idx=2, score=10)
def test_2(): ...


# * Level 2: k = 0, n <= 1e5


@subtask(idx=3, score=15)
def test_linear1():
    n = random.randint(10000, 100000)
    k = 0
    arr = [random.randint(0, 2**32) for _ in range(n)]

    X = calc_X(arr)

    return Input(arr, k), Output(X, X)


# TODO
@subtask(idx=4, score=15)
def test_linear2(): ...


# * Level 3: 0 < k < 32, n <= 1e3


@subtask(idx=5, score=10)
def test_n2_with_k1():
    n = random.randint(30, 1000)
    k = random.randint(1, 31)
    arr = [random.randint(0, 2**32) for _ in range(n)]

    X = calc_X_n_squared(arr)
    assert X == calc_X(arr)
    X_min, _ = minimize_X_n_squared(arr, k)

    return Input(arr, k), Output(X, X_min)


# TODO
@subtask(idx=6, score=10)
def test_n2_with_k2(): ...


# * Level 4: 0 < k < 32, n <= 1e5


@subtask(idx=7, score=10)
def test_linear_with_k1():
    n = 100000
    k = random.randint(1, 31)
    arr = [random.randint(0, 2**32) for _ in range(n)]

    X = calc_X(arr)
    X_min, _ = minimize_X(arr, k)

    return Input(arr, k), Output(X, X_min)


# TODO
@subtask(idx=8, score=10)
def test_linear_with_k2(): ...


# ----------------------------------- Main ----------------------------------- #

if __name__ == "__main__":
    gen_subtasks()
