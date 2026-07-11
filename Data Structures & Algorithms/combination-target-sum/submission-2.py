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
            cur.append(nums[i])
            dfs(i)
            cur.pop()
            dfs(i+1)

            return

        dfs(0)

        return res
        