class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        cur = nums.copy()

        def dfs(i, cur):
            if i >= len(nums):
                return [cur]

            # Insert index i and increment
            ins = nums[i]
            left = dfs(i+1, cur.copy()+[ins])


            # increment i until the next number is non-equivalent.
            i+=1
            while i <= len(nums)-1 and nums[i] == ins:
                i+=1
            right = dfs(i, cur)

            return left + right

        res = dfs(0, [])
        return res