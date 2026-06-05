class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        res = 0
        for i in range(n-1):
            low=prices[i]
            # Skip until prices are ascending
            if prices[i+1]<low:
                continue

            # calculate maximum profit achievable for this value
            j=i+1
            while j < n:
                profit = prices[j] - low
                res = max(profit, res)
                j+=1
        return res