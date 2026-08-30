class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = sorted(list(set(nums)))
        print(s)
        count = 1
        counts = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1] + 1:
                count += 1
            else:
                counts.append(count)
                count = 1
            print(s[i], count)
        counts.append(count)
        return max(counts)