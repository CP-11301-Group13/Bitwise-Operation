// This solution fogot to handle the edge case when k = 0, causing infinite loop.

#include <stdio.h>

#define MAX_N 400000
#define MAX_BITS 32

unsigned int arr[MAX_N];

// For debugging
void print_bins(unsigned int x) {
    for (int i = 0; i < MAX_BITS; i++) {
        printf("%d", (x >> (MAX_BITS - 1 - i)) & 1);
    }
    printf("\n");
}

int main() {
    int n, k;

    scanf("%d %d", &n, &k);

    for (int i = 0; i < n; i++) {
        scanf("%u", &arr[i]);
    }

    if (k == 32) {
        for (int i = 0; i < n; i++) {
            printf("0%c", " \n"[i == n - 1]);
        }
        return 0;
    }

    unsigned int mask_unit = (1 << k) - 1;
    unsigned int mask_low = 0, mask_high = 0;

    for (int i = 0; 2 * i * k < MAX_BITS; i++) mask_low |= mask_unit << 2 * i * k;
    for (int i = 0; (2 * i + 1) * k < MAX_BITS; i++) mask_high |= mask_unit << (2 * i + 1) * k;

    if (!((mask_low | mask_high) == ~0u && (mask_low & mask_high) == 0)) {
        printf("something wrong with the mask\n");
        return -1;
    };

    for (int i = 0; i < n; i++) {
        unsigned int res = ((arr[i] & mask_high) >> k) | ((arr[i] & mask_low) << k);
        printf("%u%c", res, " \n"[i == n - 1]);
    }
}
