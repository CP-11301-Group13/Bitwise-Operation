# Bitwise Operators Quiz 

> [!CAUTION]
> This folder is an abandoned proposal, and is kept for historical reasons. Please ignore it :)

## 說明


## Input Format 

N numbers, xi. 
Let ai be odd bits of xi, bj be even bits of xj.
Let X to be the xor sum of (ai & bj) for all i, j.

Given consider we can invert k bits, find the way to maximize X.


## Output Format


## Sample Input


## Sample Output


## Hint



給定 x1, ..., xn
令 ai 為 xi **去除偶數位** 保留奇數位；bi 為 xi **去除奇數位** 保留偶數位
例如：x = 1001, a = 10, b = 01

於是我們有兩個數列 a1, ..., an, b1, ..., bn
現在將 a,b 兩數列中的元素兩兩配對，計算 ai & bj 的 xor 和，即

$$X = \oplus_{1\leq i,j \leq n}\ a_i \land b_j $$


(Optional) 給定一個數字 k，問如何翻轉 k 個 bits 使得 X 最大化 or 最小化。

