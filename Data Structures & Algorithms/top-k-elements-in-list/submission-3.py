class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        count = sorted(count.items(), key=lambda item: item[1])
        out = []
        for i in range(-k, 0):
            out.append(count[i][0])
        return out