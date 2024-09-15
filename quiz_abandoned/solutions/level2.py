"""
O(n) solution for k=0
"""

from solution import calc_X 

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    assert len(arr) == n
    X = calc_X(arr)

    print(X, X)

