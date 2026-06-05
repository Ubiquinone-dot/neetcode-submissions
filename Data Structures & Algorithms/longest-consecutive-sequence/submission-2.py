class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        n=len(nums)
        nbreak=[]
        counter=1
        for i in range(n-1):
            if nums[i]+1 == nums[i+1]:
                counter+=1
            elif nums[i] == nums[i+1]:
                counter+=0
            else:
                nbreak.append(counter)
                counter=1
        nbreak.append(counter)
        return max(nbreak)