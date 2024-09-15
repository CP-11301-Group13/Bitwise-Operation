"""
O(n) solution for any k
"""

from solution import calc_X, minimize_X

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    assert len(arr) == n
    X = calc_X(arr)
    X_min, _ = minimize_X(arr, k)

    print(X, X_min)
