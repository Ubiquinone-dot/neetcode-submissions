class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2

        def dfs(rem, visited=set()):
            if rem == 0:
                return True
            if rem < 0:
                return False

            for i in range(len(nums)):
                if i not in visited and dfs(rem - nums[i], visited=visited | {i}):
                    return True
            return False

        return dfs(rem=target)