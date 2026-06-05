class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*n, [1]*n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        for i in list(range(0, len(nums)-1))[::-1]:
            suffix[i] = nums[i] * suffix[i+1]
        
        outs = nums
        for i in range(n):
            if i == 0:
                outs[i] = suffix[i+1]
            elif i == n-1:
                outs[i] = prefix[-2]
            else:
                outs[i] = prefix[i-1] * suffix[i+1]
    
        return outs