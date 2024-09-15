"""This script is only used for local testing. It is not used in the online judge."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from os import PathLike
from pathlib import Path
from tempfile import NamedTemporaryFile
from time import sleep, time
from typing import NamedTuple

DEFAULT_FILE = str(Path(__file__).parent / "solutions/AC1.c")

# TESTS_DIR = Path(__file__).parent / "tests"
TESTS_DIR = Path(__file__).parent
OUTPUTS_DIR = Path(__file__).parent / "outputs"
SUBTASKS_FILE = Path(__file__).parent / "subtasks.py"


class Trial(NamedTuple):
    input_name: str
    out_name: str
    time_limit: int
    memory_limit: int
    output_limit: int


@dataclass
class Subtask:
    id: int
    score: int
    trials: list[Trial]


def compare_file(file1: PathLike | str, file2: PathLike | str):
    """Return True if the two files are the same."""
    with open(file1, "r") as f1, open(file2, "r") as f2:
        while True:
            la, lb = f1.readline(), f2.readline()
            if la:
                if not lb or la.rstrip() != lb.rstrip():
                    return False
            elif lb:
                return False
            return True


class ProcessResult(Enum):
    NORMAL = 0
    RE = 1
    TLE = 2


tmp_compiled_exe = None


@lru_cache
def get_compiled_exe(filename: str) -> str:
    # set to global to prevent gc
    global tmp_compiled_exe
    tmp_compiled_exe = NamedTemporaryFile("w+b", suffix=".exe", delete=False)
    subprocess.check_output(["gcc", filename, "-o", tmp_compiled_exe.name])
    tmp_compiled_exe.close()
    return tmp_compiled_exe.name


def run(
    *,
    filename: str = DEFAULT_FILE,
    input_file: PathLike | str,
    output_file: PathLike | str,
    time_limit: int,
    memory_limit: int,
) -> ProcessResult:
    if filename.endswith(".py"):
        cmd = [sys.executable, filename]
    elif filename.endswith(".c"):
        cmd = get_compiled_exe(filename)
    else:
        cmd = filename

    with open(input_file, "r") as f_in, open(output_file, "+w") as f_out:
        # if platform.system() == "Linux":
        #     cmd = f"ulimit -v {1000};" + (cmd if isinstance(cmd, str) else " ".join(cmd))
        p = subprocess.Popen(cmd, stdin=f_in, stdout=f_out, stderr=subprocess.PIPE, shell=True)

        err = 0.3
        st = time()
        while p.poll() is None:
            if time() - st - err > time_limit:
                p.kill()
                sleep(0.1)  # wait for the process to terminate properly
                return ProcessResult.TLE
            sleep(0.1)

        return ProcessResult.NORMAL if p.returncode == 0 else ProcessResult.RE


def run_trial(filename: str, trial: Trial) -> tuple[bool, str]:
    """Run a subtask and return the result. Return True if the output is correct."""

    ifn, ofn, tl, ml, ol = trial

    output_file = OUTPUTS_DIR / ofn

    res = run(
        filename=filename,
        input_file=TESTS_DIR / ifn,
        output_file=output_file,
        time_limit=tl,
        memory_limit=ml,
    )
    if res == ProcessResult.RE:
        return False, "RE"
    elif res == ProcessResult.TLE:
        return False, "TLE"
    elif output_file.stat().st_size > ol:
        return False, "OLE"
    else:
        is_same = compare_file(output_file, TESTS_DIR / ofn)
        if not is_same:
            return False, "WA"
        return True, "AC"


def run_subtasks(filename: str, trial_ids: list[int]):
    print(f"Running {filename}")
    print()

    shutil.rmtree(OUTPUTS_DIR, ignore_errors=True)
    OUTPUTS_DIR.mkdir()

    subtasks: list[Subtask] = []

    for id, (score, *trials) in enumerate(eval(SUBTASKS_FILE.read_text())):
        subtasks.append(Subtask(id, score, list(map(Trial._make, trials))))

    total_score = 0
    for subtask in subtasks:
        print(f"===== Subtask {subtask.id} ({subtask.score}%) =====")
        if not subtask.trials:
            print("(No test cases)")
            print()
            continue

        all_passed = True

        for trial in subtask.trials:
            input_name = trial.input_name
            trial_id = int(input_name[: input_name.find(".")])

            print(f"{input_name:<6}", end="")

            if trial_ids and trial_id not in trial_ids:
                text = "SKIP"
                runtime_text = "--"
            else:
                st = time()
                is_passed, text = run_trial(filename, trial)
                all_passed = all_passed and is_passed
                run_time = time() - st
                runtime_text = f"{run_time:.2f}s"
            print(f"{' ' * 10}{text:<4} {runtime_text:>6}")

        total_score += subtask.score if all_passed else 0
        print("Score:", subtask.score if all_passed else 0)
        print()

    print()
    print(f"Total: {total_score}/100")


def main():
    parser = argparse.ArgumentParser(
        prog="Local Judge",
        description="What the program does",
        epilog="Text at the bottom of help",
    )

    parser.add_argument("filename", nargs="?", default=DEFAULT_FILE, help="Program file to run")
    parser.add_argument("trial_ids", nargs="*", type=int, help="Test ids to run")

    args = parser.parse_args()
    filename: str = args.filename
    trial_ids: list[int] = args.trial_ids

    run_subtasks(filename, trial_ids)


if __name__ == "__main__":
    main()
