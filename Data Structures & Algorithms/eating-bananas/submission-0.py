class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        low = 1
        high = max(piles)
        while low <= high:
            sunBan = 0
            mid = low + (high - low) // 2
            for pile in piles:
                sunBan += math.ceil(pile/mid)
            if (sunBan <= h):
                k = int(mid)
                high = mid - 1
            else:
                low = mid + 1
        return k
