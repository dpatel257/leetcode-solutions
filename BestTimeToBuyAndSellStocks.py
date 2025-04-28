class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = prices[0]
        for i in range(0,len(prices)):
            max_profit = max(max_profit, prices[i]-min_so_far)
            min_so_far = min(min_so_far, prices[i])
        return max_profit
