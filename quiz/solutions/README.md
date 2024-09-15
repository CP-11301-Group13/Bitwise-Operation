## 解法

### 法一：Bit masking

觀察到我們可以建立兩個 mask，分別取出高位和低位的組別，然後將他們分別右移和左移 $k$ 個位數，再將結果做 OR 運算即可。
例如要對 $x$ 的每 $k=3$ 個 bits 為一組做交換，則：

```
x              = abcdefghijkl
mask_low       = 000111000111
x & mask_low   = 000def000jkl
-----------------------------
x              = abcdefghijkl
mask_high      = 111000111000
x & mask_high  = abc000ghi000
-----------------------------
x'             = defabcjklghi
```

另外，需要注意 $k=0$ 和 $k=32$ 的特殊情況。

時間複雜度： $O(N)$

```c
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

    if (k == 0) {
        for (int i = 0; i < n; i++) {
            printf("%u%c", arr[i], " \n"[i == n - 1]);
        }
        return 0;
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

```

### 法二：Bit manipulation

除了使用 mask 之外，我們也可以直接對每個數字進行位元操作，將每 $k$ 個 bits 進行交換。

時間複雜度： $O(N\log U)$，其中 $U$ 為數字的最大值。

```c
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
    if (k == 32) {
        for (int i = 0; i < n; i++) {
            printf("0%c", " \n"[i == n - 1]);
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
        printf("%u%c", res, " \n"[i == n - 1]);
    }
}

```
