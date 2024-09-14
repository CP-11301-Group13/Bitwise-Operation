## 說明 ##

給定一個陣列，對於裡面的每個元素，請你交換其每個元素的二進制表示中的奇數位和偶數位。也就是說，位於偶數位置的bit（第`0`位、第`2`位、……）與位於奇數位置的bit（第`1`位、第`3`位、……）互換,即第`0`位跟第`1`位互換....第`30`位跟第`31`位互換。請把陣列中的每個元素做交換後輸出交換後的陣列 

## Input Format ##
第一行輸入一個整數`k`，表示有`k`組測試資料。
對於每組測試資料，先輸入一個整數`n`，表示該測試資料中的陣列大小。
接著輸入`n`個整數，表示該測試資料的陣列元素。

## Output Format ##

輸出一個整數表示交換後的結果

## Sample Input ##
```
3
3
23 43 0
4
1 2 3 4
2
4294967295 0
```

## Sample Output ##
```
43 23 0
2 1 3 8
4294967295 0
```

## Hint ##

### 解答(出的測資最好能夠在配分讓部分測資無法使用暴力通過)
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

```

