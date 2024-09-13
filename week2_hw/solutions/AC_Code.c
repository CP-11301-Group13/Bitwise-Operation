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
        int sum = prefix_sum[r] - prefix_sum[l - 1];
        printf("%d\n", sum);
    }

    return 0;
}