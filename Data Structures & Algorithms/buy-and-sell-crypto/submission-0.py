class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]

            if profit <= 0:
                l = r
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit