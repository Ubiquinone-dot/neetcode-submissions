class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(0,0): 1}
        for i in range(n):
            for j in range(m):
                if i == j and j ==0:
                    continue
                dp[(i, j)] = dp.get((i-1,j), 0) + dp.get((i,j-1), 0)
        
        print((i,j), dp)
        return dp[(n-1, m-1)]