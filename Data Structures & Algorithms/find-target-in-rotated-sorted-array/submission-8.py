class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while r >= l:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[r] < target or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            print(m, l, r)

        return -1
        # l, r = 0, len(nums)-1
        # minidx = 0
        # while r >= l:
        #     if nums[r] > nums[l]:
        #         break
        #     m = (r+l)//2

        #     # Update minimum index
        #     if nums[m] < nums[minidx]:
        #         minidx = m
            
        #     # Move pointers
        #     if nums[l] < nums[m]:  # left side sorted
        #         l = m + 1
        #         minidx = l
        #     else:
        #         if nums[r] < nums[minidx]:
        #             minidx = r
        #         r = m - 1

        # print(minidx)
        # # Unrotate array
        # def idx(i):
        #     res = i + minidx
        #     if res >= len(nums):
        #         res = res - len(nums)
        #     return res

        # l, r = 0, len(nums) - 1
        # while r >= l:
        #     m = (l+r)//2
        #     i = idx(m)
        #     print(i, m, nums, minidx)
        #     if nums[i] < target:
        #         l = m + 1
        #     elif nums[i] > target:
        #         r = m - 1
        #     else:
        #         return i

        return -1