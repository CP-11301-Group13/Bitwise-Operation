"""This script is only used for local testing. It is not used in the online judge."""

import subprocess
from pathlib import Path

# c = 'python3 -B AC_Code.py'
# c = "python -B AC_Code.py"
# c = "1189.exe"
DEFAULT_CMD = "..."
DEFAULT_OUTPUT = "slave.out"


def compare_file(file1: str, file2: str):
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


def run(*, cmd: str = DEFAULT_CMD, input_file: str, output_file: str = DEFAULT_OUTPUT):
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        p = subprocess.Popen(cmd, stdin=f_in, stdout=f_out)
        p.wait()
        return p.returncode

    # return os.system("%s < %s > %s" % (c, ifn, "slave.out"))


def main():
    output_file = DEFAULT_OUTPUT

    score = 0
    # why not just use json......
    for subtask in eval(Path("subtasks.py").read_bytes()):
        for trial in subtask[1:]:
            ifn, ofn, tl, ml, ol = trial
            print("%s " % ifn, end="")
            res = run(input_file=ifn, output_file=output_file)
            ResStr = ""
            if res != 0:
                ResStr = "RE 0"
            else:
                waLine = compare_file(output_file, ofn)
                if not waLine:
                    ResStr = "WA 0"
                else:
                    ResStr = "AC %d" % subtask[0]
                    score += subtask[0]
            print(ResStr)
    print(score)


if __name__ == "__main__":
    main()
    # what meaning does this line even have? 💀
    # input("press enter to continue...")
