class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        s = str(binary)
        count = 0
        for i in s:
            if i == "1":
                count += 1
        return count