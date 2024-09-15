### 解法

透過觀察我們發現，
$$(a\land b)\oplus(a\land c) = a \land (b\oplus c)$$
因此對於兩數列 $a_i, b_j$，

$$
\begin{align*}
\oplus_{1\leq i,j \leq n}\ a_i \land b_j &= \oplus_{1\leq i \leq n}\ a_i \land \left(\oplus_{1\leq j \leq n}\ b_j\right) \\
&= ( \oplus_{1\leq i \leq n}\ a_i ) \land ( \oplus_{1\leq j \leq n}\ b_j )
\end{align*}
$$

也就是說我們只要預先計算出 $a_i$ 和 $b_j$ 各自的 xor 和，再將兩者 AND 即可得到 $X$。

此方法的時間複雜度為 $O(n)$
