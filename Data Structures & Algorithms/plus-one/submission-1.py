class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        if digits[0] < 9:
            digits[0] += 1
        else:
            hanging = False
            for i in range(len(digits)):
                if digits[i] < 9:
                    digits[i] += 1
                    hanging = True
                    break
                else:
                    digits[i] = 0
            if hanging == False:
                digits.append(1)
        return digits[::-1]