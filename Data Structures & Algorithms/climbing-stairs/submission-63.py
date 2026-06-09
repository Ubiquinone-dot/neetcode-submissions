class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev2 = 1
        prev = 1
        
        for i in range(n-1):
            print(prev, prev2)
            tmp = prev
            prev = prev + prev2
            prev2 = tmp
        
        return prev