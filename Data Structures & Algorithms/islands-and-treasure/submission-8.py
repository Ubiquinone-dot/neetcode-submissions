class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1 
        I, J = len(grid), len(grid[0])
        visited=set()
        q = deque()

        for i in range(I):
            for j in range(J):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited|={(i,j)}

        def add(i,j):
            nonlocal visited
            if (i < 0 or j < 0 or i >= I or j >= J) or \
                (i,j) in visited or grid[i][j] == -1:
                return
            visited|={(i,j)}
            q.append([i,j])
                
        dist=0
        while q:
            for qi in range(len(q)):
                i,j = q.popleft()
                add(i,j+1)
                add(i+1,j)
                add(i,j-1)
                add(i-1,j)
                grid[i][j] = dist
            dist+=1
        
