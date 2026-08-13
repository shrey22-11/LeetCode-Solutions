class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [inf] * (amount + 1)
        dp[0] = 0   

        for x in range(1, amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], 1 + dp[x - coin])

        return dp[amount] if dp[amount] != inf else -1

        