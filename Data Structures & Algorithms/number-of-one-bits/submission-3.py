class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        for i in range(32):
            # For the nth integer, check if the AND op flips any bits: 
            flipped = n | (2**i)
            if n == flipped:
                res += 1
        
        return res