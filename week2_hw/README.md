## Problem Description

Given an array of integers, you are required to answer multiple queries. Each query asks for the sum of elements between two indices and inclusive. Your task is to implement an efficient solution to process these queries.

## Input Format

1. The first line contains two integers `n` (the size of the array) and `q` (the number of queries).
2. The second line contains `n` space-separated integers, representing the elements of the array.
3. The next `q` lines each contain two integers `l` and `r` (1-based indices), representing the range for which you need to calculate the sum of elements between index `l` and `r` (inclusive).

## Output Format

For each query, output the sum of the subarray from index `l` to `r` in a new line.

## Sample Input

```
5 3
1 2 3 4 5
1 3
2 4
1 5
```

## Sample Output

```
6
9
15
```

## Hint

To efficiently solve the problem, precompute the **prefix sum** array, where each element at index `i` stores the sum of the array elements from the start up to index `i`. Using this array, you can calculate any range sum in constant time by using the formula:

`sum(l, r) = prefix_sum[r] - prefix_sum[l-1]`

## Constraints

- 1 <= n <= 10^5 (array size)
- 1 <= q <= 10^5 (number of queries)
- 1 <= l <= r <= n
- -10^4 <= arr[i] <= 10^4 (array elements)

## Solution:

To solve the problem efficiently:

1. **Prefix Sum Approach**:
   - Prefix Sum Array: Precompute the prefix sum array in `O(n)`. This allows you to calculate the sum of any subarray in constant time by using the difference between two prefix sums.
   
2. **Query Resolution**:
   - For each query, calculate the sum of elements between `l` and `r` using the formula:

sum(l, r) = prefix_sum[r] - prefix_sum[l-1]

This makes each query take `O(1)` time.

### Full C Implementation:

```c
#include <stdio.h>

int main() {
    int n, q;
    scanf("%d %d", &n, &q);

    int arr[n + 1];
    int prefix_sum[n + 1];

    for (int i = 1; i <= n; i++) {
        scanf("%d", &arr[i]);
    }

    prefix_sum[0] = 0;
    for (int i = 1; i <= n; i++) {
        prefix_sum[i] = prefix_sum[i - 1] + arr[i];
    }

    while (q--) {
        int l, r;
        scanf("%d %d", &l, &r);

        int result = prefix_sum[r] - prefix_sum[l - 1];
        printf("%d\n", result);
    }

    return 0;
}
```