## 解法

### 法一：使用 Bit masking

時間複雜度：$O(QN)$

```c
#include <stdio.h>

#define MAXN 400000

int main() {
    int n;
    unsigned int arr[MAXN], res1[MAXN], res2[MAXN];

    scanf("%d", &n);  // 讀取整數 n，表示陣列大小

    for (int i = 0; i < n; i++) {
        scanf("%u", &arr[i]);  // 讀取陣列元素
    }

    // 任務1：交換奇偶位
    for (int i = 0; i < n; i++) {
        unsigned int N = arr[i];

        unsigned int even_bits = N & 0x55555555; // 取出偶數位
        unsigned int odd_bits = N & 0xAAAAAAAA;  // 取出奇數位

        even_bits <<= 1;  // 偶數位左移一位
        odd_bits >>= 1;   // 奇數位右移一位

        res1[i] = even_bits | odd_bits;  // 結合奇偶位
    }

    // 輸出任務1結果
    for (int i = 0; i < n; i++) {
        printf("%u", res1[i]);
        if (i != n - 1) printf(" ");
    }
    printf("\n");

    // 任務2：交換相鄰的 bit pack
    for (int i = 0; i < n; i++) {
        unsigned int N = arr[i];

        unsigned int lower_mask = 0x33333333; // 00110011001100110011001100110011
        unsigned int upper_mask = 0xCCCCCCCC; // 11001100110011001100110011001100

        unsigned int lower_bits = N & lower_mask;
        unsigned int upper_bits = N & upper_mask;

        lower_bits <<= 2;  // 下位元組左移2位
        upper_bits >>= 2;  // 上位元組右移2位

        res2[i] = lower_bits | upper_bits;
    }

    // 輸出任務2結果
    for (int i = 0; i < n; i++) {
        printf("%u", res2[i]);
        if (i != n - 1) printf(" ");
    }
    printf("\n");

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
        scanf("%u", &arr[i]);  // 讀取陣列元素
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
            printf(" ");  // 輸出空格分隔
        }
    }
    printf("\n");  // 輸出結束後換行

    // 任務2：交換相鄰的 bit pack
    for (int i = 0; i < n; i++) {
        unsigned int N = arr[i];
        unsigned int brute_result = 0;

        for (int j = 0; j < 32; j += 4) {
            // 取出相鄰的兩個 bit pack（每個 bit pack 有兩個位元）
            unsigned int bit_pack1 = (N >> j) & 0b11;       // 取出第 j 和 j+1 位
            unsigned int bit_pack2 = (N >> (j + 2)) & 0b11; // 取出第 j+2 和 j+3 位

            // 交換這兩個 bit pack
            brute_result |= (bit_pack1 << (j + 2));  // 將 bit_pack1 移到位置 j+2 和 j+3
            brute_result |= (bit_pack2 << j);        // 將 bit_pack2 移到位置 j 和 j+1
        }

        printf("%u", brute_result);

        if (i != n - 1) {
            printf(" ");  // 輸出空格分隔
        }
    }
    printf("\n");  // 輸出結束後換行

    return 0;
}
```
