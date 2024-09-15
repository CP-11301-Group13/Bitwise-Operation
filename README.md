# Bitwise Operations

Group 20

## Directory Structure

We have two folders `hw`, `quiz`, each for a problem. The structure of each folder is as follows:

```plaintext
hw
├── README.md           # Problem description
├── gen_tests.py        # Test case generator
├── judge.py            # Local judge
├── solutions           # Solutions & AC codes
│   ├── AC.py
│   ├── AC.c
│   └── README.md       # Solution description
├── special
├── subtasks.py         # Problem subtasks
└── tests               # Test cases
    ├── *.in
    └── *.out
```

## Run judge locally

```bash
# Windows
python judge.py <program_file> [input_id, ...]
# Linux
python3 judge.py <program_file> [input_id, ...]


# Example: run `AC1.py` with all tests in `tests/`
python judge.py solutions/AC1.py
# Example: run `AC1.py` with `1.in` and `3.in`
python judge.py solutions/AC1.py 1 3
# Example: run judge with C file
python judge.py solutions/AC1.c
# Example: run judge with executable file
gcc solutions/AC1.c; python judge.py ./a.out
```

## Git Workflow

1. `git pull`
2. `git commit -m '<message describing what you have done>'`
3. `git push`
