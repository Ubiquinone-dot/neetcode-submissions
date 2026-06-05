class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)

        ans=[]
        for i in range(N):
            for j in range(N):
                if j <= i:
                    continue

                if nums[i] + nums[j] == target:
                    return [i, j]