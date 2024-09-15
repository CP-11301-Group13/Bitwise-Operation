"""
O(n^2) solution for any k
"""

from solution import calc_X_n_squared, minimize_X_n_squared

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    assert len(arr) == n
    X = calc_X_n_squared(arr)
    X_min, _ = minimize_X_n_squared(arr, k)

    print(X, X_min)
