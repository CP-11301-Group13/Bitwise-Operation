MAXN = 400000

def main():
    n = int(input())  # 讀取整數 n，表示陣列大小
    arr = list(map(int, input().split()))  # 讀取n個元素

    res1 = [0] * n
    res2 = [0] * n

    # 任務1：交換奇偶位
    for i in range(n):
        N = arr[i]

        even_bits = N & 0x55555555  # 取出偶數位
        odd_bits = N & 0xAAAAAAAA   # 取出奇數位

        even_bits <<= 1  # 偶數位左移一位
        odd_bits >>= 1   # 奇數位右移一位

        res1[i] = even_bits | odd_bits  # 結合奇偶位

    # 輸出任務1結果
    print(" ".join(map(str, res1)))

    # 任務2：交換相鄰的 bit pack
    for i in range(n):
        N = arr[i]

        lower_mask = 0x33333333  # 00110011001100110011001100110011
        upper_mask = 0xCCCCCCCC  # 11001100110011001100110011001100

        lower_bits = N & lower_mask
        upper_bits = N & upper_mask

        lower_bits <<= 2  # 下位元組左移2位
        upper_bits >>= 2  # 上位元組右移2位

        res2[i] = lower_bits | upper_bits

    # 輸出任務2結果
    print(" ".join(map(str, res2)))


if __name__ == "__main__":
    main()
