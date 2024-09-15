## 說明 ##

給定一個陣列，對於裡面的每個元素請你完成下面兩個任務:
1. 請你交換其每個元素的二進制表示中的奇數位和偶數位。也就是說，位於偶數位置的bit（第`0`位、第`2`位、……）與位於奇數位置的bit（第`1`位、第`3`位、……）互換,即第`0`位跟第`1`位互換....第`30`位跟第`31`位互換。請把陣列中的每個元素做交換後輸出交換後的陣列。   
例如:   
 $$
\begin{align*}
    &a = 1254\ (\text{decimal}) =  00000000000000000000010011100110\ (\text{binary})\\[10pt]
    &\text{after transaction} =
        \overbrace{0}^{a_{31}}\ \overbrace{0}^{a_{30}}\ \overbrace{0}^{a_{29}}\ \overbrace{0}^{a_{28}}\ \overbrace{0}^{a_{27}}\
        \ \cdots\ \ 
        \overbrace{1}^{a_4}\ \overbrace{1}^{a_3}\ \overbrace{0}^{a_2}\ \overbrace{0}^{a_1}\ \overbrace{1}^{a_0} \\[10pt]
    &\text{after swapping odd and even bits} =
        \overbrace{0}^{a_{31}}\ \overbrace{0}^{a_{30}}\ \overbrace{0}^{a_{29}}\ \overbrace{0}^{a_{28}}\ \overbrace{0}^{a_{27}}\
        \ \cdots\ \ 
        \overbrace{0}^{a_4}\ \overbrace{1}^{a_3}\ \overbrace{0}^{a_2}\ \overbrace{1}^{a_1}\ \overbrace{0}^{a_0} = 2265\\[10pt]
    &\text{correct output} =2265
         \\[10pt]
\end{align*}

$$


2. 接下來的任務是，從第`0`位開始到第`31`位，將相鄰的兩個 bit 組成一個 bit pack。例如，第`0`和第`1`位組成一個 `bit pack`，第`2`和第`3`位組成另一個`bit pack`，以此類推。接著，你需要交換每個奇數位和偶數位的`bit pack`，即將每個`bit pack`中的奇數位和偶數位對調。   
例如:   
 A = `1254`(decimal) = `00000000 00000000 0000 01 00 11 10 01 10`(binary)   
 經過奇偶`bit pack`交換後會得到`00000000 00000000 000000 01 10 11 10 01`   
 可以看到相鄰的兩個`bit pack`被交換了如員數組中的第一個`bit pack`為
$$
\begin{align*}
    &a = 1254\ (\text{decimal}) =  00000000000000000000010011100110\ (\text{binary})\\[10pt]
    &\text{after transaction} =
        \overbrace{00}^{a_{15}}\ \overbrace{00}^{a_{14}}\ \overbrace{00}^{a_{13}}\ \overbrace{00}^{a_{12}}\ \overbrace{00}^{a_{11}}\
        \ \cdots\ \ 
        \overbrace{00}^{a_4}\ \overbrace{11}^{a_3}\ \overbrace{10}^{a_2}\ \overbrace{01}^{a_1}\ \overbrace{10}^{a_0} \\[10pt]
    &\text{after swapping odd and even bits} =
        \overbrace{00}^{a_{15}}\ \overbrace{00}^{a_{14}}\ \overbrace{00}^{a_{13}}\ \overbrace{00}^{a_{12}}\ \overbrace{00}^{a_{11}}\
        \ \cdots\ \ 
        \overbrace{01}^{a_4}\ \overbrace{10}^{a_3}\ \overbrace{11}^{a_2}\ \overbrace{10}^{a_1}\ \overbrace{01}^{a_0}=441\\[10pt]
    &\text{correct output} = 441
\end{align*}


$$
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
3
23 43 0
4
1 2 3 4
2
4294967295 0
```

## Sample Output ##
```
43 23 0
77 142 0
2 1 3 8
4 8 12 1
4294967295 0
4294967295 0
```

## Hint ##
Using the bit mask trick.   
How to extract the odd bit and even bit by using `&` ?   
after that you should do some bit shifting  and combine them.
