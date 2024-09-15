## 解法

### 法一：使用 Bit masking

時間複雜度：$O(QN)$

```c
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

    return 0;
}
```

### 法二：直接遍例每個 bit

時間複雜度：$O(QN\log U)$，其中 $U$ 是輸入的最大整數

```c
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
            unsigned int result = 0;

            // 遍歷每個bit，逐位進行奇偶交換
            for (int bit = 0; bit < 32; bit++) {
                unsigned int current_bit = (N >> bit) & 1; // 取出第bit位
                if (bit % 2 == 0) {
                    // 偶數位，應該放到奇數位
                    result |= current_bit << (bit + 1);
                } else {
                    // 奇數位，應該放到偶數位
                    result |= current_bit << (bit - 1);
                }
            }

            printf("%u", result);

            if (i != n - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}


```
