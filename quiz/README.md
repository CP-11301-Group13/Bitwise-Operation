# 位元序順不響影閱讀

## 背景故事

> Credit: [Github Copilot](https://github.com/features/copilot)

在你成功地解決了位元能量異常現象後，數位星球的秩序逐漸恢復。然而，新的挑戰接踵而至。這次，星球上的能量數據變得更加複雜，並且需要更高效的處理方式來確保星球的穩定。

為了應對這一挑戰，你需要進一步優化能量單元的排列方式。具體而言，除了之前的位元交換操作，現在還需要考慮更大範圍內的位元組合和重組。這將要求你在處理數據時，能夠靈活地應用不同的分組大小和交換策略，以達到最佳的能量流動效果。

你的新任務是針對每個能量單元，將其位元以 k 為一組。接者，你需要將每兩組位元進行交換，以實現能量的最佳流動。通過這種方式，你將能夠更有效地重塑能量的分佈，並且進一步提高星球的能量穩定性。這將進一步鞏固數位星球的秩序，確保其長久的穩定與繁榮。

## 說明

給定 $N$ 個 **32 位元無號整數** $a_1, ..., a_N$ 和 $k$，請將 $a_i$ 的 bits 以 $k$ 為一組，自低位起對每兩組進行交換，將結果輸出。

具體而言，考慮 $a = 00100110$， $k=2$，則分組方式為：

$$
a = \overbrace{00}^{a_3} \enspace\overbrace{10}^{a_2} \enspace\overbrace{01}^{a_1} \enspace\overbrace{10}^{a_0}
$$

將 $a_0$ 與 $a_1$ 交換， $a_2$ 與 $a_3$ 交換，得到

$$
a' = \overbrace{10}^{a_2} \enspace\overbrace{00}^{a_3} \enspace \overbrace{10}^{a_0} \enspace\overbrace{01}^{a_1}
$$

如果 $2k$ 無法整除 $32$，則先將 $a$ 的高位補零使其總位數為 $2k$ 的倍數（即補零後的總位數為 $2k\cdot\left\lceil\frac{32}{2k}\right\rceil$），再進行交換，最後將結果取 $32$ 位元。例如 $a=3061544883, k=6$：

$$
\begin{align}
    &a = 10 \enspace\overbrace{110110}^{a_4} \enspace\overbrace{011110}^{a_3}\enspace\overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_1}\enspace\overbrace{110011}^{a_0} \\
    \Rightarrow \quad  &\tilde{a} =
        \overbrace{000010}^{a_5}\enspace\overbrace{110110}^{a_4}\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_1}\enspace\overbrace{110011}^{a_0}\enspace\\
    &\tilde{a}' =
        \overbrace{110110}^{a_4}\enspace\overbrace{000010}^{a_5}\enspace  \overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110011}^{a_0}\enspace\overbrace{011110}^{a_1}\enspace\\
    &a' =
         \overbrace{10}^{a_4}\enspace\overbrace{000010}^{a_5} \enspace
         \overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110011}^{a_0}\enspace\overbrace{011110}^{a_1}\enspace\\
\end{align}
$$

上式的 $a'$ 即為所求。請注意：你的程式碼並不一定需要計算出 $\tilde{a}$ 和 $\tilde{a}'$，這裡僅是為了說明補零的過程。換言之，本題可以僅使用 32 位元無號整數完成，而不需要用到 `long int`。

## Input Format

輸入共有兩行，第一行為兩個整數 $N$ 和 $k$，由空格分開；第二行為 $N$ 個整數 $a_1, ..., a_N$，由空格分開。

-   $0 < N \leq 4\cdot 10^4$
-   $0 \leq a_i < 2^{32}$
-   $0 \leq k \leq 32$

## Output Format

輸出一行，為 $a_1, ..., a_N$ 交換後的結果。請以十進位數字輸出，並以空格分開。

## Sample Input 1

```
4 1
10 12 14 0
```

## Sample Output 1

```
5 12 13 0
```

### 說明

```
10 => 1010 => 0101 => 5
12 => 1100 => 1100 => 12
14 => 1110 => 1101 => 13
0  => 0000 => 0000 => 0
```


## Sample Input 2

```
1 1
3061544883
```

## Sample Output 1

```
2195582174
```

### 說明

```
3061544883 
=> 10_110110_011110_110111_011110_110011 
=> 10_000010_110111_011110_110011_011110  
=> 2195582174
```


## 測資

### Subtask 0-1 (10%)

-   $0 < n \leq 100$
-   $0\leq a_i < 2^{16}$
-   $k = 1$

### Subtask 2-3 (10%)

-   $0 < n \leq 100$
-   $0\leq a_i < 2^{16}$
-   $k = 2$

### Subtask 4-5 (20%)

-   $0 < n \leq 4\cdot 10^5$
-   $0\leq a_i < 2^{32}$
-   $k = 2$

### Subtask 6-7 (20%)

-   $0 < n \leq 4\cdot 10^5$
-   $0\leq a_i < 2^{32}$
-   $1 \leq k \leq 32$
-   $k = 2^m,\ m\in \mathbb{N}$

### Subtask 8-9 (20%)

-   $0 < n \leq 4\cdot 10^5$
-   $0\leq a_i < 2^{16}$
-   $0 \leq k \leq 32$

### Subtask 10-11 (20%)

-   $0 < n \leq 4\cdot 10^5$
-   $0\leq a_i < 2^{32}$
-   $0 \leq k \leq 32$

## Hint

請仔細注意測資邊界條件

## Bonus

> 純屬娛樂，沒有分數

這是星球上某個遠古文明所遺留的一串密碼，你能夠解讀出其中的秘密嗎？

Hint: 將密碼 base64 decode 後，每四個 bytes 組成一個 32 位元無號整數 (little endian)，並以某個 $k$ 進行本題的交換操作。至於 $k$ 要怎麼找到呢？據說解開的秘密是由 `https://` 開頭的一段文字，請根據這個線索，使用你的頭腦來暴力破解吧。

```
hkdHBzej8vJ3d3fil/ZXR1cmVuI29tbydxZHNobzZ9NGFXdDd5N1doU2FQA=
```
