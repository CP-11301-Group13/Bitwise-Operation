#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);  // 讀取整數 n，表示陣列大小

    unsigned int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%u", &arr[i]);  // 讀取n個元素
    }

    // 任務1：交換奇數位和偶數位
    for (int i = 0; i < n; i++) {
        unsigned int N = arr[i];
        unsigned int brute_result = 0;

        for (int j = 0; j < 32; j += 2) {
            unsigned int even_bit = (N >> j) & 1;      // 取出偶數位 (第 j 位)
            unsigned int odd_bit = (N >> (j + 1)) & 1; // 取出奇數位 (第 j+1 位)

            // 交換位元
            brute_result |= (even_bit << (j + 1));  // 偶數位放到奇數位
            brute_result |= (odd_bit << j);         // 奇數位放到偶數位
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