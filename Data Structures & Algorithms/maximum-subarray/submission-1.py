class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        count = 0
        for i in nums:
            count += i
            maxSum = max(maxSum, count)
            if count < 0:
                count = 0
        return maxSum

