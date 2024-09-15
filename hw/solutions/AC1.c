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
            unsigned int even_bits = N & 0x55555555; // 取出偶數位
            unsigned int odd_bits = N & 0xAAAAAAAA;  // 取出奇數位

            even_bits <<= 1; // 偶數位左移一位
            odd_bits >>= 1;  // 奇數位右移一位

            unsigned int result = even_bits | odd_bits;
            printf("%u", result);

            if (i != n - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
}
  