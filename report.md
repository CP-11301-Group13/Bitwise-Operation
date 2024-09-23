# Homework

# Quiz

# 位元序順不響影閱讀

## Motivation

本題中，你的任務是有效地重組能量，以確保數位星球的能量流動達到最佳狀態。該挑戰需要熟悉位元操作，每個能量單元的位元將按照大小為 `k` 的區段進行分組，並交換相鄰區段，以穩定星球的能量流動。本題要求你能夠高效地處理大量 32 位元無號整數的位元。

## Problem

給定 `N` 個 **32 位元無號整數** `a_1, ..., a_N` 和一個**非負整數** `k`，任務是將每個整數的位元以大小為 `k` 的區段進行分組，然後交換每對相鄰的區段。你需要對陣列中的每個整數執行並輸出結果。如果總位數無法被 `2k` 整除，則需要在最後的區段補零以完成交換。

舉例來說，對於 `a = 00100110` and `k=2`，會變：

```
a = 00 10 01 10
```

進行位元變換之後，結果會變：

```
a = 10 00 10 01
```

計算並輸出每個輸入整數重新排列後的值。

## Solution

要想通過本題，我們建議使用bitmask。首先，透過bit shifting與其他常見位元操作（主要是AND），創建針對低位區段和高位區段的bitmask。此演算法可以通過but shifting與bitmask確保解決方案在相對於輸入大小的時間複雜度為$O(n)$。此外，提供的解決方案也處理了 `k=0` 或 `k=32` 的邊界情況，以及需要補零的情況。

## Code

為了解決這個問題，程式碼通過位元操作和遮罩來完成分組與交換的功能。首先，程式接收兩個輸入值：整數 `N` 代表輸入的數量，整數 `k` 代表需要分組的位元大小。接著，程式會依次讀取 `N` 個 32 位元無號整數並將其存儲在陣列 `arr[]` 中。

此演算法的核心邏輯在於透過位元遮罩的應用來對每個數字進行分組和交換。程式首先根據 `k` 值建立一個單位遮罩 `mask_unit`，這個遮罩用來捕捉一組位元。接著，利用 `mask_unit` 分別創建低位區段遮罩 `mask_low` 和高位區段遮罩 `mask_high`。這些遮罩會透過位移操作確保對應的位元分組能夠準確地被擷取和交換。

一旦遮罩建立完畢，程式會檢查遮罩是否正確。如果遮罩無法正確覆蓋所有位元區段，則程式將輸出錯誤訊息並結束運行。當遮罩正確時，程式對每個數字進行操作，透過將高位區段向右移位並將低位區段向左移位，來達成分組後的交換。最終的結果會被輸出為重新排列後的數字。

此外，程式還考慮了特殊邊界情況：當 `k=0` 時，意味著不需要任何分組與交換，因此直接輸出原始數據；當 `k=32` 時，則所有位元都被覆蓋並交換，最終結果將為全0。

這個解決方案的時間複雜度為 $O(n)$，其中 `n` 是輸入的數量。由於操作僅涉及位元運算和遮罩應用，因此綜觀來說沒有太高複雜度。

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

## Test Data

The testing process involved input files of various complexities to evaluate the efficiency and accuracy of the applied solution. These files contained large arrays of 32-bit unsigned integers with both small and large values to test how well the algorithm handles bit exchanges. The test cases included inputs where `k=1`, `k=2`, and larger values, with edge cases such as zero-padding required due to non-divisible lengths. The solution was rigorously tested to ensure it handles all cases effectively, from arrays with the maximum allowed length to simpler, smaller test cases. Each test case successfully returned the expected results, validating the solution's robustness across different input scenarios.
