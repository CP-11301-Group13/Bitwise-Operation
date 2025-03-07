#include <stdio.h>

int main() {
    int k;
    scanf("%d", &k);

    for (int t = 0; t < k; t++) {
        int n;
        scanf("%d", &n);

        unsigned int arr[n];
        for (int i = 0; i < n; i++) {
            scanf("%u", &arr[i]);
        }

        for (int i = 0; i < n; i++) {
            unsigned int N = arr[i];
            unsigned int brute_result = 0;
            for (int j = 0; j < 32; j += 2) {
                unsigned int even_bit = (N >> j) & 1;
                unsigned int odd_bit = (N >> (j + 1)) & 1;

                // 交換位元
                brute_result |= (even_bit << (j + 1));
                brute_result |= (odd_bit << j);
            }
            printf("%u", brute_result);

            if (i != n - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}