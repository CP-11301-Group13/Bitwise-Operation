# Homework：二進制之亂，奇偶能量的平衡之道

## Motivation

考量到本題為第二周的作業，在不確定大家的實力基礎下，我們不希望加入太多額外的演算法要素，而是以較為基礎的題目來帶領大家熟悉基本的 bitwise operations。對於已經熟悉的同學，也可以學到 constant bit mask 的小技巧。此外，這個問題也可以延伸到 quiz 的題目中。

## Problem

給定一個整數 $k$ ，表示有 $k$ 組能量數據。接著輸入一個整數 $n$ ，表示該能量數據中的陣列大小。接著輸入 $n$ 個 **32 位元無號整數**，每個整數以空白間隔，表示該能量數據的陣列元素。任務是將每個整數的位元作「奇數位」和「偶數位」交換。
奇偶數位的規則為由 least significant bit 從 $0$ 開始計算，直到第 $31$ 位。例如： $12 = 1101$ 的奇數位為 $10$，偶數位為 $11$。

計算並輸出每個輸入整數奇偶交換後的值。

## Solution

### $O(1)$ 解法

1. 輸入解析：
   讀取測試數量 k。對於每個測試，讀取整數數量 n，然後讀取由 n 個 32 位元無號整數組成的 list。
2. 位元提取： 對於列表中的每個整數，我們使用位元遮罩提取偶數位（偶數位置的位元）和奇數位（奇數位置的位元）：
    - 使用 mask 0x55555555 提取偶數位（位於 0, 2, 4, …, 30 的位元）。
    - 使用 mask 0xAAAAAAAA 提取奇數位（位於 1, 3, 5, …, 31 的位元）。
3. 位元移動： 提取位元後:
    - 將偶數位左移 1 個位置，將它們移到奇數位位置。
    - 將奇數位右移 1 個位置，將它們移到偶數位位置。
4. 結合結果： 將移動後的偶數位和奇數位通過位元 OR (|) 操作符結合，形成每個整數的最終結果。
5. 輸出結果： 修改後的整數將按照輸入的順序列印出來。

### $O(\log U)$ 解法

除了上述解法外，亦可以迴圈遍例所有 bits，並兩兩交換。此方法的時間複雜度為 $O(\log U)$，其中 $U$ 是整數的最大值。

## Code

時間複雜度為每個測試案例 $O(n)$，其中 n 是整數的數量。由於我們只進行位元運算和簡單的算術操作，每個整數在固定時間內被處理，因此本演算法對於大量輸入也相當高效。

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
            unsigned int even_bits = N & 0x55555555;  // 取出偶數位
            unsigned int odd_bits = N & 0xAAAAAAAA;   // 取出奇數位

            even_bits <<= 1;  // 偶數位左移一位
            odd_bits >>= 1;   // 奇數位右移一位

            unsigned int result = even_bits | odd_bits;
            printf("%u", result);

            if (i != n - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
}
```

## Testdata

測資方面，我們的測資數量隨著 subtask 的分配，呈現指數等級成長在，最後一筆測資有大約 160000 筆，試圖要求答題者使用我們要求的演算法，在 edge case 的部分我們簡單的考慮了 0 的情況，在大多數的解法下不會造成太大的困難。

## Teamwork

### People

| 姓名   | 學號      | 系級   |
| ------ | --------- | ------ |
| 洪愷希 | B10401006 | 醫學四 |
| 何宗蕘 | B11801005 | 公衛三 |
| 陳澤諒 | B12505047 | 工海二 |
| 張玉慧 | B12902090 | 資工二 |
| 温文安 | R13944053 | 網媒一 |

### 出題

-   故事：何宗蕘
-   題目：温文安
-   AC Code：温文安
-   測資：張玉慧
-   校對：何宗蕘
-   課堂報告：洪愷希

### 撰寫報告

-   Motivation/Problem：何宗蕘
-   Solution/Code：陳澤諒
-   Test Data/Teamwork/Reference：温文安

## Reference

> Credit: [geekforgeeks](https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/)

# Quiz：位元序順不響影閱讀

## Motivation

本題是承接 hw 的題目，希望訓練大家 generalization 的能力，並且透過一些 edge cases（例如 $2k$ 無法整除 $32$） 來測試同學是否能謹慎思考每一個步驟對應的可能情況。

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

要想通過本題，我們建議使用 bitmask。首先，透過 bit shifting 與其他常見位元操作（主要是 AND），創建針對低位區段和高位區段的 bitmask。此演算法可以通過 but shifting 與 bitmask 確保解決方案在相對於輸入大小的時間複雜度為$O(n)$。此外，提供的解決方案也處理了 `k=0` 或 `k=32` 的邊界情況，以及需要補零的情況。

## Code

為了解決這個問題，程式碼通過位元操作和遮罩來完成分組與交換的功能。首先，程式接收兩個輸入值：整數 `N` 代表輸入的數量，整數 `k` 代表需要分組的位元大小。接著，程式會依次讀取 `N` 個 32 位元無號整數並將其存儲在陣列 `arr[]` 中。

此演算法的核心邏輯在於透過位元遮罩的應用來對每個數字進行分組和交換。程式首先根據 `k` 值建立一個單位遮罩 `mask_unit`，這個遮罩用來捕捉一組位元。接著，利用 `mask_unit` 分別創建低位區段遮罩 `mask_low` 和高位區段遮罩 `mask_high`。這些遮罩會透過位移操作確保對應的位元分組能夠準確地被擷取和交換。

一旦 bitmask 建立完畢，程式會檢查 mask 是否正確。如果 mask 無法正確覆蓋所有位元區段，則程式將輸出錯誤訊息並結束運行。當遮罩正確時，程式對每個數字進行操作，透過將高位區段向右移位並將低位區段向左移位，來達成分組後的交換。最終的結果會被輸出為重新排列後的數字。

此外，程式還考慮了特殊邊界情況：當 `k=0` 時，意味著不需要任何分組與交換，因此直接輸出原始數據；當 `k=32` 時，則所有位元都被覆蓋並交換，最終結果將為全 0。

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

測資涉及多種不同複雜度的輸入文件，以評估所應用解決方案的效率和準確性。這些文件包含大量 32 位元無號整數的陣列，數值範圍從小到大，用以測試算法在位元交換處理上的表現。測試案例涵蓋了不同的 `k` 值，包含 `k=1`、`k=2` 等較小值，以及更大的 `k` 值，同時也測試了當位數無法被 `2k` 整除時需要補零的邊界情況。

## Teamwork

### People

| 姓名   | 學號      | 系級   |
| ------ | --------- | ------ |
| 洪愷希 | B10401006 | 醫學四 |
| 何宗蕘 | B11801005 | 公衛三 |
| 陳澤諒 | B12505047 | 工海二 |
| 張玉慧 | B12902090 | 資工二 |
| 温文安 | R13944053 | 網媒一 |

### 出題

-   故事：張玉慧
-   題目：洪愷希
-   AC Code：洪愷希
-   測資：陳澤諒
-   校對：張玉慧
-   課堂報告：温文安

### 撰寫報告

-   Motivation/Problem：何宗蕘
-   Solution/Code：陳澤諒
-   Test Data/Teamwork/Reference：洪愷希

## Reference

None

# 學習單排序

2 > 8 > 1 > 3 > 21 > 6 > 4 > 15 > 18 > 12 > 9 > 10 > 17 > 13 > 19 > 11 > 14 > 16 > 7
