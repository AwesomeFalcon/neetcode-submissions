class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (r - l) // 2 + l
            time = 0
            for i in piles:
                time += math.ceil(float(i) / m)
            if time > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res