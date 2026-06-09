class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(c) for c in 
            (str(int(''.join([str(c) for c in digits]))+1))
        ]