class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1
        if count1 == count2:
            return True
        for r in range(len(s1), len(s2)):
            count2[s2[r]] += 1

            l = s2[r - len(s1)]
            count2[l] -= 1
            if count2[l] == 0:
                del count2[l]
            if count1 == count2:
                return True
        return False