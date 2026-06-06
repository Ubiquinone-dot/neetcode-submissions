class Solution:
    
    # def binary_search(self, l, r, nums, target):        
    #     if l > r:
    #         return -1

    #     # Find midpoint; middle of r-l window offset by l
    #     mid = l + ((r - l ) // 2) # floored.

    #     if nums[mid] == target:
    #         return mid
        
    #     if nums[mid] < target:
    #         # must be on upper half
    #         return self.binary_search(mid+1, r, nums, target)
    #     else:
    #         return self.binary_search(l, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        # return self.binary_search(0, len(nums) - 1, nums, target)

        l, r = 0, len(nums)-1

        while l <= r:

            mid = l + ((r - l) // 2)

            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
            
        return -1


