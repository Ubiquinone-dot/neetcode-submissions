class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        cur = []

        def dfs(i):
            if sum(cur) > target or i >= len(nums):
                return
            elif sum(cur) == target:
                res.append(cur.copy())
                return
            dfs(i+1)
            cur.append(nums[i])
            dfs(i)
            cur.pop()

            return

        dfs(0)

        return res
        