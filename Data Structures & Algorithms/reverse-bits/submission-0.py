class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = s.zfill(32)
        s = s[::-1]
        print(s)
        return int(s,2)