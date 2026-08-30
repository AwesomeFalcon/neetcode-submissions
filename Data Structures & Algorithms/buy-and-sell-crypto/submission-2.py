class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
            profit = max(profit, i - lowest)
        return profit