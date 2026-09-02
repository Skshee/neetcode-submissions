class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float('inf')
        best = 0

        for i in range(len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]

            best = max(best, prices[i]-currMin)
        return best