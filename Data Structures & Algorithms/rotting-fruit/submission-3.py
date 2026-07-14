class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        visit=set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit|={(i,j)}
        
        def add(i,j):
            nonlocal visit
            nonlocal grid
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or\
                (i,j) in visit or grid[i][j] == 0:
                return False
            visit |= {(i,j)}
            q.append([i,j])
            grid[i][j] = 2
            return True
        res = 0
        while q:
            anyy = False
            for qi in range(len(q)):
                i, j = q.popleft()
                anyy = any([
                    add(i,j+1),
                    add(i+1,j),
                    add(i,j-1),
                    add(i-1,j)
                ]) or anyy
            if anyy:
                res+=1

        # check all are gone
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res 