## 說明 ##

給定一個無號的32位整數`N`，請你交換其二進制表示中的奇數位和偶數位。也就是說，位於偶數位置的bit（第0位、第2位、……）與位於奇數位置的bit（第1位、第3位、……）互換,即第0位跟第1位互換....第30位跟第31位互換。輸出交換後的無號整數。 

## Input Format ##
第一行輸入`k`表示有`k`組測資   
第二行包含一個整數`N`表示要進行交換的無號整數   

## Output Format ##

輸出一個整數表示交換後的結果

## Sample Input ##
```
3
23
43
0

```

## Sample Output ##
```
43
23
0
```

## Hint ##

### 解答(出的測資最好能夠在配分上一部分能把第二個暴力的做法下來)
```c
#include <stdio.h>
int main() {
    int k;
    

    scanf("%d", &k);

    for (int i = 0; i < k; i++) {
        unsigned int N;
        scanf("%u", &N);

        unsigned int even_bits = N & 0x55555555; // 0x55555555 = 01010101...0101
        unsigned int odd_bits = N & 0xAAAAAAAA;  // 0xAAAAAAAA = 10101010...1010

        even_bits <<= 1; 
        odd_bits >>= 1; 

        unsigned int result = even_bits | odd_bits;
        printf("%u\n", result);

    }

    return 0;
}
```
```c
#include <stdio.h>
int main() {
    int k;
    
    scanf("%d", &k);

    for (int i = 0; i < k; i++) {  
        unsigned int N;
        scanf("%u", &N);     
        // --- 解法二：暴力解法 ---
        unsigned int brute_result = 0;
        for (int j = 0; j < 32; j += 2) {
            unsigned int even_bit = (N >> j) & 1;      
            unsigned int odd_bit = (N >> (j + 1)) & 1; 

            // 交換
            brute_result |= (even_bit << (j + 1)); 
            brute_result |= (odd_bit << j);       
        }

        printf("%u\n", brute_result);
    }

    return 0;
}
```

