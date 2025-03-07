"""This script is only used for local testing. It is not used in the online judge."""

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from os import PathLike
from pathlib import Path
from time import sleep, time
from typing import NamedTuple

# c = 'python3 -B AC_Code.py'
# c = "python -B AC_Code.py"
# c = "1189.exe"
DEFAULT_FILE = str(Path(__file__).parent / "solutions/ac_code.py")

TESTS_DIR = Path(__file__).parent / "tests"
OUTPUTS_DIR = Path(__file__).parent / "outputs"
SUBTASKS_FILE = Path(__file__).parent / "subtasks.py"


class Config(NamedTuple):
    input_name: str
    out_name: str
    time_limit: int
    memory_limit: int
    output_limit: int


@dataclass
class Subtask:
    score: int
    config: Config


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


def run(
    *,
    filename: str = DEFAULT_FILE,
    input_file: PathLike | str,
    output_file: PathLike | str,
    time_limit: int,
) -> ProcessResult:
    if filename.endswith(".py"):
        cmd = [sys.executable, filename]
    else:
        raise ValueError("Invalid file type")

    with open(input_file, "r") as f_in, open(output_file, "+w") as f_out:
        p = subprocess.Popen(cmd, stdin=f_in, stdout=f_out)

        err = 0.3
        st = time()
        while p.poll() is None:
            if time() - st - err > time_limit:
                p.kill()
                return ProcessResult.TLE
            sleep(0.1)
        return ProcessResult.NORMAL if p.returncode == 0 else ProcessResult.RE


def run_subtask(filename: str, subtask: Subtask) -> tuple[bool, str]:
    """Run a subtask and return the result. Return True if the output is correct."""

    ifn, ofn, tl, ml, ol = subtask.config

    output_file = OUTPUTS_DIR / ofn

    res = run(
        filename=filename,
        input_file=TESTS_DIR / ifn,
        output_file=output_file,
        time_limit=tl,
    )
    if res == ProcessResult.RE:
        return False, "RE"
    elif res == ProcessResult.TLE:
        return False, "TLE"
    else:
        is_same = compare_file(output_file, TESTS_DIR / ofn)
        if not is_same:
            return False, "WA"
        return True, "AC"


def run_subtasks(filename: str, test_ids: list[int]):
    print(f"Running {filename}")
    print()

    shutil.rmtree(OUTPUTS_DIR, ignore_errors=True)
    OUTPUTS_DIR.mkdir()

    subtasks: list[Subtask] = []
    for score, *trials in eval(SUBTASKS_FILE.read_text()):
        assert len(trials) == 1, trials
        subtasks.append(Subtask(score, Config(*trials[0])))

    total_score = 0
    for subtask in subtasks:
        input_name = subtask.config.input_name
        subtask_id = input_name[: input_name.find(".")]

        if test_ids and subtask_id not in test_ids:
            continue

        print(f"{input_name:<6} ", end="")
        has_score, text = run_subtask(filename, subtask)
        total_score += subtask.score if has_score else 0
        print(f"{text:>4}   {subtask.score if has_score else 0 :>3}/{subtask.score:>3}")

    print()
    print(f"Total: {total_score}/100")


def main():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )

    parser.add_argument("filename", help="Program file to run")
    parser.add_argument("test_ids", nargs="*", type=int, help="Test ids to run")

    args = parser.parse_args()
    filename: str = args.filename
    test_ids: list[int] = args.test_ids

    run_subtasks(filename, test_ids)


if __name__ == "__main__":
    main()
