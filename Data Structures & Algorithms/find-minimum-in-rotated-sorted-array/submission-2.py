class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while r >= l:
            m = (r+l)//2

            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            res = min(nums[m], res)
            if nums[l] > nums[m]:
                r = m - 1  # in left segmnt
            else:
                l = m + 1  # in right segment

        return res