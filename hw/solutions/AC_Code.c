#include <stdio.h>
int main() {
    int k;
    

    scanf("%d", &k);

    for (int i = 0; i < k; i++) {
        unsigned int N;
        scanf("%u", &N);

        unsigned int even_bits = N & 0x55555555; // 0x55555555 = 01010101...0101
        unsigned int odd_bits = N & 0xAAAAAAAA;  // 0xAAAAAAAA = 10101010...1010

        even_bits <<= 1; 
        odd_bits >>= 1; 

        unsigned int result = even_bits | odd_bits;
        printf("%u\n", result);

    }

    return 0;
}