class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def get(i):
            return dp.get(i, [nums[i]])
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(*nums)
        
        # Where the zeroth index may be chosen, disallowing -1
        dp = [n for n in nums]
        dp[1] = max(dp[0], dp[1])
        
        # Where the zeroth index is never chosen, allowing -1
        dpw= [n for n in nums]
        dpw[0] = 0 
        for i in range(2, len(nums)):
            if i == len(nums)-1:
                res = max(dp[i-2], dp[i-1]) # zeroth value was counted so cannot count i
                resw = max(nums[i] + dpw[i-2], dpw[i-1])
                print(res, resw)
                return max(res, resw)

            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            dpw[i] = max(nums[i] + dpw[i-2], dpw[i-1])
            print(i, dp, dpw)

