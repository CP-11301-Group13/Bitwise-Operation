"""
The difficulty of testcase should be classified into 4 main levels:

1. (10%) 0 <= n <= 100,   arr[i] <= 2**16, k = 1
2. (10%) 0 <= n <= 100,   arr[i] <= 2**16, k = 2
3. (20%) 0 <= n <= 4*1e5, arr[i] <= 2**32, k = 2
4. (20%) 0 <= n <= 4*1e5, arr[i] <= 2**32, k <= 32, k = 2**m for some m
5. (20%) 0 <= n <= 4*1e5, arr[i] <= 2**16, 0 <= k <= 32
6. (20%) 0 <= n <= 4*1e5, arr[i] <= 2**32, 0 <= k <= 32

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
from functools import partial
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
    arr: list[int]

    def format(self):
        return f"{" ".join(map(str, self.arr))}"


TrialFunc = Callable[[], tuple[Input, Output]]
WrappedTrialFunc = Callable[[], bool]


TESTS_DIR = Path(__file__).parent / "tests"
SUBTASKS_FILE = Path(__file__).parent / "subtasks.py"


class Manager:
    def __init__(self, *, scores: list[int]) -> None:
        self.scores = scores
        self.trial_funcs: list[dict[int, WrappedTrialFunc]] = [{} for _ in scores]
        self.trial_ids: set[int] = set()

    def trial(
        self, *, subtask_id: int, trial_id: int | None = None
    ) -> Callable[[TrialFunc], WrappedTrialFunc]:
        if trial_id is None:
            trial_id = len(self.trial_ids)

        if subtask_id >= len(self.scores):
            raise ValueError("Invalid subtask_id")
        if trial_id in self.trial_ids:
            raise ValueError("Duplicate trial_id")
        self.trial_ids.add(trial_id)

        def wrap(func: TrialFunc) -> WrappedTrialFunc:
            def new_func():
                try:
                    in_str, out_str = func()

                    in_file = TESTS_DIR / f"{trial_id}.in"
                    in_file.write_text(in_str.format())
                    out_file = TESTS_DIR / f"{trial_id}.out"
                    out_file.write_text(out_str.format())
                    return True
                except TypeError:
                    print(
                        f"WARNING: Failed generating trail {func.__name__} of subtask {subtask_id}"
                    )
                    return False

            self.trial_funcs[subtask_id][trial_id] = new_func
            return new_func

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
                    print(f"WARNING: Trial {trial_id} failed")
                if time() - st > TIME_LIMIT:
                    print(f"WARNING: Trial {trial_id} is too slow")

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

"""
0. (10%) n <= 2**16, k = 1
1. (10%) n <= 2**16, k = 2
2. (20%) n <= 2**32, k = 2
3. (20%) n <= 2**32, k <= 32, k = 2**m for some m
4. (20%) n <= 2**16, 0 <= k <= 32
5. (20%) n <= 2**32, 0 <= k <= 32
"""


def solve(arr: list[int], k: int) -> list[int]:
    res = list(map(partial(swap_k_groups, k=k), arr))
    res_str = list(map(partial(swap_k_groups_str, k=k), arr))
    assert res == res_str
    return res


# * Subtask 0


# if trial_id is not provided, it will be automatically assigned
@manager.trial(subtask_id=0)
def test_example() -> tuple[Input, Output]:
    """Example test case, should be public."""

    k = 1
    arr = [0b1010, 0b1100, 0b1111, 0b0000]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


@manager.trial(subtask_id=0, trial_id=1)
def test_1() -> tuple[Input, Output]:
    n = random.randint(1, 2**16)
    k = 1
    arr = [random.randint(0, 2**32 - 1) for _ in range(n)]
    res = solve(arr, k)

    return Input(arr, k), Output(arr=res)


# ----------------------------------- Main ----------------------------------- #

if __name__ == "__main__":
    manager.gen_subtasks()
