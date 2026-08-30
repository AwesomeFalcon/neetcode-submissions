class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = []
        while n != 1:
            s = str(n)
            sum = 0
            for i in s:
                sum += (pow(int(i),2))
            n = sum
            if n in numbers:
                return False
            else:
                numbers.append(n)
        return True