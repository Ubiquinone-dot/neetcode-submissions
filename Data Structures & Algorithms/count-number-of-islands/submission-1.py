class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        I, J = len(grid), len(grid[0])
        visited = set()
        # from functools import cache
        # @cache
        def dfs(i, j):
            nonlocal visited
            nonlocal grid
            if i >= I or j >= J or i < 0 or j < 0:
                return False
            if (i,j) in visited:
                return False

            if grid[i][j] == "1":
                visited |= {(i,j)}
                return (
                    dfs(i+1,j) or 
                    dfs(i,j+1) or 
                    dfs(i-1,j) or
                    dfs(i,j-1)
                )
            else:
                return False

        res = 0
        for i in range(I):
            for j in range(J):
                if grid[i][j]=="1" and (i,j) not in visited:
                    print(i,j, visited)
                    dfs(i, j)
                    res+=1

        return res