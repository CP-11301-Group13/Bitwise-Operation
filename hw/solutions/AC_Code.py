k = int(input()) 
for _ in range(k):
    n = int(input())  
    arr = list(map(int, input().split()))  

    for i in range(n):
        N = arr[i]
        even_bits = N & 0x55555555  # 取出偶數位
        odd_bits = N & 0xAAAAAAAA   # 取出奇數位

        even_bits <<= 1  # 偶數位左移一位
        odd_bits >>= 1   # 奇數位右移一位

        result = even_bits | odd_bits
        print(result, end=" " if i != n - 1 else "\n")  
