# Bitwise Operators Quiz (Team 13)

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

如果 $2k$ 無法整除 $32$，則可視為在 $a$ 的高位補上 $2k\cdot\left\lceil\frac{32}{2k}\right\rceil$ 個 $0$ 後，再將交換後的結果取 $32$ 位元。例如 $k=6$：

$$
\begin{align*}
    &a = 10\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_1}\enspace\overbrace{110011}^{a_0} \\
    \Rightarrow \quad  &\tilde{a} =
        \overbrace{000000}^{a_5}\enspace\overbrace{000010}^{a_4}\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_1}\enspace\overbrace{110011}^{a_0}\enspace\\
    &\tilde{a}' =
        \overbrace{000010}^{a_4}\enspace\overbrace{000000}^{a_5}\enspace  \overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110011}^{a_0}\enspace\overbrace{011110}^{a_1}\enspace\\
    &a' =
         \overbrace{00}^{a_5} \enspace
         \overbrace{110111}^{a_2}\enspace\overbrace{011110}^{a_3}\enspace\overbrace{110011}^{a_0}\enspace\overbrace{011110}^{a_1}\enspace\\
\end{align*}
$$

上式的 $a'$ 即為所求。

## Input Format

輸入共有兩行，第一行為兩個整數 $N$ 和 $k$，由空格分開；第二行為 $N$ 個整數 $a_1, ..., a_N$，由空格分開。

-   $0 < N \leq 400000$
-   $0 \leq k \leq 32$
-   $0 \leq a_i < 2^{32}$

## Output Format

輸出一行，為 $a_1, ..., a_N$ 交換後的結果。請以十進位數字輸出，並以空格分開。

## Sample Input

```
4 1
10 12 15 0
```

## Sample Output

```
5 12 13 0
```

### 說明

```
10 => 1010 => 0101 => 5
12 => 1100 => 1100 => 12
15 => 1110 => 1101 => 13
0  => 0000 => 0000 => 0
```
