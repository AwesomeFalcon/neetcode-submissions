class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for i in nums:
            if i == 0:
                red += 1
            if i == 1:
                white += 1
            if i == 2:
                blue += 1
        j = 0
        for i in range(red):
            nums[j] = 0
            j += 1
        for i in range(white):
            nums[j] = 1
            j += 1
        for i in range(blue):
            nums[j] = 2
            j += 1
            