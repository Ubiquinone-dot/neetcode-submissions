class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = [
            [n for i,n in enumerate(nums) if i != j]
            for j in range(len(nums))
        ]
        outs=[]
        for lst in d:
            v = 1
            for v2 in lst:
                v *= v2
            outs.append(
                v
            )

        return outs