class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, buying=False) - prices[i]
                cool = dfs(i+1, buying=True)
                dp[(i, buying)] = max(buy, cool)
            else:
                sell = dfs(i+2, buying=True) + prices[i]
                cool = dfs(i+1, buying=False)
                dp[(i, buying)] = max(sell, cool)
            return dp[(i, buying)]
        return dfs(0, True)
        
        # n = len(prices)
        # dp = {}
        # for i in range(n-1,-1,-1):
        #     for j in range(n-1, i-1, -1):
        #         # if selling today, then take diagonal next
        #         dp[(i,j)] = max(
        #             dp.get((i+1,j+1), 0) + (prices[j] - prices[i]),  # sell today
        #             dp.get((i, j+1), 0)
        #         )
        # return dp[(0,0)]