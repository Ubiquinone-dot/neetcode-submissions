class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        
        triplets = []
        visited = []
        
        for k in range(n):
            left = k+1
            right = n - 1

            while left < right:
                total = nums[k] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                    continue
                elif total > 0:
                    right -= 1
                    continue
                else:
                    vals = sorted([nums[k], nums[left], nums[right]])
                    idxs = sorted([k, left, right])
                    if vals not in triplets and idxs not in visited and len(set(idxs))==len(idxs):
                        triplets.append(vals)
                        visited.append(idxs)
                    left+=1
                
        return [list(t) for t in triplets]