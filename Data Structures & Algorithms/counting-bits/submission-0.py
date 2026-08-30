class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0, n + 1):
            binary = bin(i)
            string = str(binary)
            count = 0
            for i in string:
                if i == "1":
                    count += 1
            output.append(count)
        return output