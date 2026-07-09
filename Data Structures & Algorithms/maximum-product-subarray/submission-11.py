class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = curmin = 1
        res=max(nums)

        for n in nums:
            if n==0:
                curmin, curmax = 1, 1
                continue
            tmp = curmax * n
            curmax = max(n*curmax, n*curmin, n)
            curmin = min(tmp, n*curmin, n)
            res = max(res, curmax)

        return res

        # if len(nums) == 1:
        #     return nums[0]
        # res = nums[0]

        # for i in range(len(nums)):
        #     prod=nums[i]
        #     res=max(prod, res)
        #     for j in range(i+1, len(nums)):
        #         prod *= nums[j]
        #         res = max(prod, res)

        return res