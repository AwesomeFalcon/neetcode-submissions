class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, n in enumerate(nums):
            j = target - n
            if j in sums:
                return [sums[j], i]
            sums[n] = i