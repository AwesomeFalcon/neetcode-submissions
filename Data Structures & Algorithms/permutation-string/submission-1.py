class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        for i in s1:
            count1[i] += 1
        for i in range(0, len(s2) - len(s1) + 1):
            count2 = defaultdict(int)
            for j in range(len(s1)):
                count2[s2[i + j]] += 1
            if count2 == count1:
                return True
        return False