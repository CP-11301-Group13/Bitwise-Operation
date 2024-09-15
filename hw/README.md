## 說明 ##

給定`N`個無號整數，對於每個無號整數請你完成下面兩個任務:
1. task1，請你交換該整數的二進制表示中的奇數位和偶數位。也就是說，位於偶數位置的bit（第`a0`、第`a2`、……）與位於奇數位置的bit（`a1`、`a3`、……）互換,即第`a0`跟第`a1`互換....`a30`跟第`a31`互換。請你輸出交換後的 
例如:   
 $$
\begin{align*}
    &a = 1254\ (\text{decimal}) = 00000000000000000000010011100110\ (\text{binary})\\
    &\text{after swapping odd and even bits} = 0_{a_{31}}\ 0_{a_{30}}\ 0_{a_{29}}\ 0_{a_{28}}\ 0_{a_{27}}\ \cdots\ 0_{a_4}\ 1_{a_3}\ 0_{a_2}\ 1_{a_1}\ 0_{a_0} = 2265\\
    &\text{correct output} = 2265
\end{align*}
$$


2. task2，從第`0`位開始到第`31`位，將相鄰的兩個 bit 組成一個 bit pack。例如，第`0`和第`1`位組成一個 `bit pack`，第`2`和第`3`位組成另一個`bit pack`形成bit packs `a0` 到 `a15`，以此類推。接著，你需要交換每個奇數位和偶數位的`bit pack`，也就是位於偶數位置的bit pacjs（`a0`、`a2`、……）與位於奇數位置的bit packs（`a1`、`a3`、……）互換,即`a0`跟`a1`互換....`a14`跟第`a15`互換   
例如:   

$$
\begin{align*}
    &a = 1254\ (\text{decimal}) = 00_{a_{15}}\ 00_{a_{14}}\ 00_{a_{13}}\ 00_{a_{12}}\ 00_{a_{11}}\ \cdots\ 00_{a_4}\ 11_{a_3}\ 10_{a_2}\ 01_{a_1}\ 10_{a_0}\ (\text{binary})\\
    &\text{after swapping odd and even bit packs} = 00_{a_{15}}\ 00_{a_{14}}\ 00_{a_{13}}\ 00_{a_{12}}\ 00_{a_{11}}\ \cdots\ 01_{a_4}\ 10_{a_3}\ 11_{a_2}\ 10_{a_1}\ 01_{a_0} = 441\\
    &\text{correct output} = 441
\end{align*}
$$
3. 這兩個task是獨立的task，注意請不要拿task1的輸出來做task2，確保兩個task的輸入使用的都是原始的輸入。
## Input Format ##
輸入共有兩行，第一行為一個整數 $N$ ，由空格分開；第二行為 $N$ 個整數 $a_1, ..., a_N$，由空格分開。

-   $0 < N \leq 400000$
-   $0 \leq a_i < 2^{32}$

## Output Format ##
輸出有兩行:   
第一行輸出`n`個整數 表示陣列中每個元素做奇偶位交換後的結果   
第二行輸出`n`個整數 表示陣列中每個`bit pack`做奇偶交換的結果

## Sample Input ##
```
9
23 43 0 1 2 3 4 4294967295 0
```
## Sample Output ##
```
43 23 0 2 1 3 8 4294967295 0
77 142 0 4 8 12 1 4294967295 0
```

## Hint ##
Using the bit mask trick.   
How to extract the odd bit and even bit by using `&` ?   
after that you should do some bit shifting  and combine them.
