class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        bitmask = bin(n)
        res += sum([1 for j in range(len(bitmask)) if bitmask[j] == '1']) 
        return res