# 解法

## 計算 $X$

透過觀察我們發現，
$$(a\land b)\oplus(a\land c) = a \land (b\oplus c)$$
因此對於兩數列 $a_i, b_j$，

$$
\begin{align*}
\oplus_{1\leq i,j \leq n}\ a_i \land b_j &= \oplus_{1\leq i \leq n}\ a_i \land \left(\oplus_{1\leq j \leq n}\ b_j\right) \\
&= ( \oplus_{1\leq i \leq n}\ a_i ) \land ( \oplus_{1\leq j \leq n}\ b_j )
\end{align*}
$$

也就是說我們只要預先計算出 
$$A := \oplus_{1\leq i \leq n}\ a_i$$
$$B := \oplus_{1\leq j \leq n}\ b_j$$
則 $X = A\land B$。
<!-- $a_i$ 和 $b_j$ 各自的 xor 和，再將兩者 AND 即可得到 $X$。 -->


此方法的時間複雜度為 $O(n)$

## 翻轉 $k$ 個 bits 使 $X$ 最小

為了使 $X$ 最小，我們希望讓最高位的 $k$ 非零 bits 變為 $0$。令 $X[i]$ 表示 $X$ 的第 $i$ 個 bit，則 $X[i] = 1 $ 若且惟若 $A[i]=1$ 且 $B[i]=1$。因此我們只要翻轉 $A[i]$ 或是 $B[i]$，就可以使 $X[i]=0$。

我們知道對於 $x\oplus y$，若翻轉 $x$ 的第 $i$ 個 bit，則 $x\oplus y$ 也會翻轉第 $i$ 個 bit。因此我們只要翻轉任意 $a_j[i]$，就可以翻轉 $A[i]$（對於 $B[i]$ 同理）。

當我們要翻轉 $X[i]$ 時，我們可以任意選擇一個 $j$，並且翻轉 $a_j[i]$ 或是 $b_j[i]$。注意到 $b_j[i] = x_j[2i]$，所以我們可以將 $x_j$ 的第 $2i$ 個 bit翻轉，這樣就可以翻轉 $X[i]$。

綜上所述，我們首先要找出 $X$ 最高位且非零的 $k$ 個 bits，然後對於每個 $i$ 任選 $x_j$ 並翻轉 $x_j[2i]$，即可最小化 $X$。這樣的時間複雜度為 $O(n)$。