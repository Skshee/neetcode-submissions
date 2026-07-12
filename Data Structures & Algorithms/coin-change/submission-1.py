class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in memo:
                return memo[i]

            memo[i] = 1 + min(dp(i - coin) for coin in coins)
            return memo[i]

        memo = {}      
        ways = dp(amount)
        return ways if dp(amount) != float('inf') else -1
        
