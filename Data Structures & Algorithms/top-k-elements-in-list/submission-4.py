class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        heap = []
        for i in count.keys(): 
            heapq.heappush(heap, (count[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res