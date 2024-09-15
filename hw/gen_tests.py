"""
Subtasks:

0. (10%) 0 < n <= 100,   arr[i] < 2**8
1. (10%) 0 < n <= 100,   arr[i] < 2**16
2. (20%) 0 < n <= 4*1e5, arr[i] < 2**16
3. (20%) 0 < n <= 4*1e5, arr[i] < 2**32

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

# --------------------------------- Constants -------------------------------- #

random.seed("CP113-1 RANDOM SEED")

TIME_LIMIT = 2
MEMORY_LIMIT = 64 << 20
OUTPUT_LIMIT = 64 << 16


# ---------------------------------- Helpers --------------------------------- #


@dataclass
class Input:
    arrs: list[list[int]]

    def format(self):
        Q = len(self.arrs)
        return f"{Q}\n" + "\n".join(f"{len(arr)}\n" + " ".join(map(str, arr)) for arr in self.arrs)


@dataclass
class Output:
    arrs: list[list[int]]

    def format(self):
        return "\n".join(" ".join(map(str, arr)) for arr in self.arrs)


TrialFunc = Callable[[], tuple[Input, Output]]
WrappedTrialFunc = Callable[[], bool]


TESTS_DIR = Path(__file__).parent / "tests"
SUBTASKS_FILE = Path(__file__).parent / "subtasks.py"


def parse_output(output: str) -> str:
    output = output.replace("\r\n", "\n")
    assert len(output) <= OUTPUT_LIMIT, f"Output limit exceeded: {len(output)} > {OUTPUT_LIMIT}"
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
                    except TypeError:
                        print(
                            f"WARNING: Failed generating trail {func.__name__} of subtask {subtask_id}"
                        )
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

SCORES = [15, 15, 35, 35]

manager = Manager(scores=SCORES)

"""
0. (15%) 0 < Q <= 10,  0 < n <= 100,  arr[i] < 2**8
1. (15%) 0 < Q <= 10,  0 < n <= 100,  arr[i] < 2**16
2. (35%) 0 < Q <= 200, 0 < n <= 200,  arr[i] < 2**16
3. (35%) 0 < Q <= 200, 0 < n <= 2000, arr[i] < 2**32
"""


def solve(arrs: list[list[int]]) -> list[list[int]]:
    res = []
    for arr in arrs:
        row = []
        for x in arr:
            even_bits = x & 0x55555555  # 取出偶數位
            odd_bits = x & 0xAAAAAAAA  # 取出奇數位

            even_bits <<= 1  # 偶數位左移一位
            odd_bits >>= 1  # 奇數位右移一位

            row.append(even_bits | odd_bits)
        res.append(row)
    return res


# * Subtask 0


# if trial_id is not provided, it will be automatically assigned
@manager.trial(subtask_ids=0)
def test_sample() -> tuple[Input, Output]:
    """Sample test case, should be public."""

    arrs = [
        [23, 43, 0],
        [1, 2, 3, 4],
    ]
    res = solve(arrs)

    return Input(arrs), Output(arrs=res)


# * Subtask 1:  0 < n <= 100,   arr[i] < 2**16


@manager.trial(subtask_ids=1)
def test_sub1():
    Q = random.randint(6, 10)
    n = random.randint(50, 100)

    arrs = [[random.randint(0, 2**16 - 1) for _ in range(n)] for _ in range(Q)]
    res = solve(arrs)
    return Input(arrs), Output(arrs=res)


# * Subtask 2:  0 < Q <= 200, 0 < n <= 200,  arr[i] < 2**16


@manager.trial(subtask_ids=2)
def test_sub2():
    Q = random.randint(100, 200)
    n = random.randint(100, 200)

    arrs = [[random.randint(0, 2**16 - 1) for _ in range(n)] for _ in range(Q)]
    res = solve(arrs)
    return Input(arrs), Output(arrs=res)


# * Subtask 3:  0 < Q <= 200, 0 < n <= 2000, arr[i] < 2**32


@manager.trial(subtask_ids=3)
def test_sub3():
    Q = random.randint(100, 200)
    n = random.randint(1000, 2000)

    arrs = [[random.randint(0, 2**32 - 1) for _ in range(n)] for _ in range(Q)]
    res = solve(arrs)
    return Input(arrs), Output(arrs=res)


# ----------------------------------- Main ----------------------------------- #

if __name__ == "__main__":
    manager.gen_subtasks()
