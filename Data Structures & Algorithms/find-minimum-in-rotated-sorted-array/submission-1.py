class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minNum = nums[low]
        while low < high:
            med = low + (high - low) // 2
            minNum = min(minNum, nums[med])
            if nums[med] > nums[high]:
                low = med + 1
            else:
                high = med - 1
        return min(minNum, nums[low])