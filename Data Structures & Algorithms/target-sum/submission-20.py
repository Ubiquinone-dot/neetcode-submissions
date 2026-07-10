class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return int(abs(nums[0]) == abs(target))
        
        res = 0
        from functools import cache
        # @cache
        def dfs(rem, i):
            if i >= len(nums):
                return int(rem == 0)
            add = dfs(rem + nums[i], i+1) 
            sub = dfs(rem - nums[i], i+1)
            return add + sub
        
        return dfs(target, 0)
