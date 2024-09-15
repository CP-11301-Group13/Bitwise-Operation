// Solving with direct bit manipulation

#include <stdio.h>

#define MAX_N 400000
#define MAX_K 32
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

    if (k == 0) {
        for (int i = 0; i < n; i++) {
            printf("%u%c", arr[i], " \n"[i == n - 1]);
        }
        return 0;
    }

    unsigned int mask_unit = (1 << k) - 1;

    for (int i = 0; i < n; i++) {
        unsigned int res = 0, origin = arr[i], mask = mask_unit;
        for (int i = 0; i < MAX_BITS; i += 2 * k) {
            unsigned int low = origin & mask;
            mask <<= k;
            unsigned int high = origin & mask;
            mask <<= k;
            res |= (low << k) | (high >> k);
        }
        // print_bins(arr[i]);
        // print_bins(res);
        printf("%u%c", res, " \n"[i == n - 1]);
    }
}
