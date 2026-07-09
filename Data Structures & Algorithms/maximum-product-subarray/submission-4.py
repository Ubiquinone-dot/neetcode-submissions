class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        res = nums[0]

        for i in range(len(nums)):
            prod=nums[i]
            res=max(prod, res)
            for j in range(i+1, len(nums)):
                prod *= nums[j]
                res = max(prod, res)

        return res