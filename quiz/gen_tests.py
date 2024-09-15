"""
Subtasks:

0. (10%) 0 < n <= 100,   arr[i] < 2**16, k = 1
1. (10%) 0 < n <= 100,   arr[i] < 2**16, k = 2
2. (20%) 0 < n <= 4*1e5, arr[i] < 2**32, k = 2
3. (20%) 0 < n <= 4*1e5, arr[i] < 2**32, 1 <= k <= 32, k = 2**m for some m
4. (20%) 0 < n <= 4*1e5, arr[i] < 2**16, 0 <= k <= 32
5. (20%) 0 < n <= 4*1e5, arr[i] < 2**32, 0 <= k <= 32

---

Format of `subtasks.py`:

[score, [input_file, output_file, time_limit, memory_limit, output_limit]]
"""

from __future__ import annotations

import json
import random
import shutil
from dataclasses import dataclass
from functools import partial, wraps
from pathlib import Path
from time import time
from typing import Callable

from solutions.solution import (
    swap_k_groups,
    swap_k_groups_str,
)

# --------------------------------- Constants -------------------------------- #

random.seed("CP113-1 RANDOM SEED")

TIME_LIMIT = 2
MEMORY_LIMIT = 64 << 24
OUTPUT_LIMIT = 64 << 16


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
    arr: list[int]

    def format(self):
        return f"{" ".join(map(str, self.arr))}"


TrialFunc = Callable[[], tuple[Input, Output]]
WrappedTrialFunc = Callable[[], bool]


TESTS_DIR = Path(__file__).parent / "tests"
SUBTASKS_FILE = Path(__file__).parent / "subtasks.py"


def parse_output(output: str) -> str:
    output = output.replace("\r\n", "\n")
    assert len(output) <= OUTPUT_LIMIT, f"Output length is {len(output)} > {OUTPUT_LIMIT}"
    return output


class Manager:
    def __init__(self, *, scores: list[int]) -> None:
        self.scores = scores
        self.trial_funcs: list[dict[int, WrappedTrialFunc]] = [{} for _ in scores]
        self.trial_ids: set[int] = set()
        self.called_trials: set[int] = set()

    def trial(
        self, *, subtask_ids: int | list[int], trial_id: int | None = None
    ) -> Callable[[TrialFunc], TrialFunc]:
        """
        Parameters:
            subtask_id: index of the subtask
            triad_id: the name of test data file, e.g. triad_id=1 => 1.in, 1.out
        """

        if isinstance(subtask_ids, int):
            subtask_ids = [subtask_ids]

        if trial_id is None:
            trial_id = len(self.trial_ids)

        if trial_id in self.trial_ids:
            raise ValueError("Duplicate trial_id")
        self.trial_ids.add(trial_id)

        def wrap(func: TrialFunc) -> TrialFunc:
            for subtask_id in subtask_ids:
                if subtask_id >= len(self.scores):
                    raise ValueError("Invalid subtask_id")

                @wraps(func)
                def new_func():
                    if trial_id in self.called_trials:
                        return True
                    self.called_trials.add(trial_id)

                    try:
                        in_str, out_str = func()

                        in_file = TESTS_DIR / f"{trial_id}.in"
                        in_file.write_text(in_str.format())
                        out_file = TESTS_DIR / f"{trial_id}.out"
                        out_file.write_text(parse_output(out_str.format()))
                        return True
                    except TypeError as e:
                        print(
                            f"WARNING: Failed generating trail {func.__name__} of subtask {subtask_id}; trial_id {trial_id}."
                        )
                        print("Error:", e)
                        return False

                self.trial_funcs[subtask_id][trial_id] = new_func
            return func

        return wrap

    def gen_subtasks(self, *idxs: int):
        shutil.rmtree(TESTS_DIR, ignore_errors=True)
        TESTS_DIR.mkdir()

        subtask_trial_ids = []
        for subtask_id, func in enumerate(manager.trial_funcs):
            suc_ids = []

            if idxs and subtask_id not in idxs:
                continue

            for trial_id, func in func.items():
                st = time()
                if func():
                    suc_ids.append(trial_id)
                else:
                    # print(f"WARNING: Trial {trial_id} failed")
                    pass
                if time() - st > TIME_LIMIT * 2:  # double because we solve with two methods
                    print(f"WARNING: Trial {trial_id} is too slow. (function: {func.__name__})")

            subtask_trial_ids.append(suc_ids)
            if not suc_ids:
                print(f"WARNING: No successful trials for subtask {subtask_id}")

        # score_map_suc = {
        #     idx: score for idx, score in score_map.items() if subtask_suc.get(idx, False)
        # }
        expected_trial_cnt = max(len(self.trial_ids), max(self.trial_ids) + 1)
        if self.trial_ids != (expected_ids := set(range(expected_trial_cnt))):
            missing_ids = expected_ids - self.trial_ids
            print(f"WARNING: Subtask ids are missing: {sorted(missing_ids)}")
        if sum(self.scores) != 100:
            print(f"WANRING: Sum of scores is not 100: {sum(self.scores)}")

        with open(SUBTASKS_FILE, "+w") as f:
            subtasks_spec = [
                [
                    score,
                    *(
                        [
                            f"{trial_id}.in",
                            f"{trial_id}.out",
                            TIME_LIMIT,
                            MEMORY_LIMIT,
                            OUTPUT_LIMIT,
                        ]
                        for trial_id in trial_ids
                    ),
                ]
                for score, trial_ids in zip(self.scores, subtask_trial_ids)
            ]
            # we should manual format the file
            json.dump(subtasks_spec, f)


# --------------------------------- Subtasks --------------------------------- #

SCORES = [10, 10, 20, 20, 20, 20]

manager = Manager(scores=SCORES)


def solve(arr: list[int], k: int) -> list[int]:
    res = list(map(partial(swap_k_groups, k=k), arr))
    res_str = list(map(partial(swap_k_groups_str, k=k), arr))
    assert res == res_str
    return res


# * Subtask 0:  0 <= n <= 100, arr[i] <= 2**16, k = 1


# if trial_id is not provided, it will be automatically assigned
@manager.trial(subtask_ids=0)
def test_sample() -> tuple[Input, Output]:
    """Sample test case, should be public."""

    k = 1
    arr = [0b1010, 0b1100, 0b1110, 0b0000]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


@manager.trial(subtask_ids=0)
def test_sub0() -> tuple[Input, Output]:
    n = random.randint(30, 100)
    k = 1
    arr = [random.randint(2**8, 2**16 - 1) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


@manager.trial(subtask_ids=0)
def test_edge1() -> tuple[Input, Output]:
    n = 100
    k = 1
    arr = [(1 << 16) - random.randint(0, 2**8) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# * Subtask 1:  0 <= n <= 100,   arr[i] < 2**16, k = 2


@manager.trial(subtask_ids=1)
def test_sub1() -> tuple[Input, Output]:
    n = random.randint(30, 100)
    k = 2
    arr = [random.randint(2**8, 2**16) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


@manager.trial(subtask_ids=1)
def test_edge2() -> tuple[Input, Output]:
    n = 100
    k = 2
    arr = [(1 << 16) - random.randint(0, 2**8) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# * Subtask 2:  0 <= n <= 4*1e5, arr[i] < 2**32, k = 2


@manager.trial(subtask_ids=2)
def test_sub2() -> tuple[Input, Output]:
    n = random.randint(10000, 400000)
    k = 2
    arr = [random.randint(2**16, 2**32) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# * Subtask 3:  0 <= n <= 4*1e5, arr[i] < 2**32, 1 <= k <= 32, k = 2**m for some m


@manager.trial(subtask_ids=[3, 4, 5])
def test_edge_k_is_32() -> tuple[Input, Output]:
    n = random.randint(10000, 400000)
    k = 32
    arr = [random.randint(0, 2**16 - 1) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


@manager.trial(subtask_ids=3)
def test_sub3() -> tuple[Input, Output]:
    n = random.randint(10000, 400000)
    k = 2 ** random.randint(0, 5)
    arr = [random.randint(2**16, 2**32) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# * Subtask 4:  0 <= n <= 4*1e5, arr[i] < 2**16, 0 <= k <= 32


@manager.trial(subtask_ids=[4, 5])
def test_edge_k_is_zero() -> tuple[Input, Output]:
    n = random.randint(10000, 400000)
    k = 0
    arr = [random.randint(0, 2**16 - 1) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


@manager.trial(subtask_ids=4)
def test_sub4() -> tuple[Input, Output]:
    n = random.randint(10000, 400000)
    k = random.randint(0, 32)
    arr = [random.randint(2**8, 2**16) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# * Subtask 5:  0 <= n <= 4*1e5, arr[i] < 2**32, 0 <= k <= 32


@manager.trial(subtask_ids=5)
def test_sub5() -> tuple[Input, Output]:
    n = random.randint(10000, 400000)
    k = random.randint(0, 31)
    arr = [random.randint(2**16, 2**32) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# ----------------------------------- Main ----------------------------------- #

if __name__ == "__main__":
    manager.gen_subtasks()
