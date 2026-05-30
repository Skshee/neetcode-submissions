class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    maxProfit = max(profit, maxProfit)

        return maxProfit