class Solution:
    def checkValidString(self, s: str) -> bool:
        min = 0
        max = 0
        for i in s:
            if i == "(":
                max += 1
                min += 1
            elif i == ")":
                max -= 1
                min -= 1
            else:
                min -= 1
                max += 1
            if max < 0:
                return False
            if min < 0:
                min = 0
        return min == 0

            