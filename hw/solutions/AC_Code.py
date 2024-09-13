
k = int(input())

for _ in range(k):

    N = int(input())


    even_bits = N & 0x55555555  
    odd_bits = N & 0xAAAAAAAA   

    even_bits <<= 1  
    odd_bits >>= 1  

    result = even_bits | odd_bits  


    print(result)
