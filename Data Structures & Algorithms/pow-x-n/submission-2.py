class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            sum = x
            for i in range(n - 1):
                sum = x * sum
        elif n == 0:
            sum = 1
        else:
            sum = 1
            for i in range(abs(n)):
                sum = sum / x
        return sum