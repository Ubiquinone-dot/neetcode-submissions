class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:    
        dp = {c: 1 for c in coins}
        coins = sorted(coins, reverse=True)
        if amount==0:
            return 0

        def dfs(left):
            if left in dp:
                return dp[left]
            found=False
            for c in coins:
                rem = left - c
                if rem > 0:
                    dfs(rem)
                    if dp.get(rem, -1) > 0:
                        dp[left] = min(dp[rem] + 1, dp.get(left, float('inf')))
                        found=True

            if not found:
                dp[left] = -1
            return

        dfs(amount)
        print(dp)
        return dp[amount]