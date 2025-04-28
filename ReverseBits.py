class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        for i in range(0,32):
            #print((n >> i) & 1)
            new_n = new_n | (((n >> i) & 1) << (31 - i))
        
        #print(new_n)
        return new_n

        
