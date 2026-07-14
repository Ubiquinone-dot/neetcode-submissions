

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visit = set(starts)
            q = deque(starts)
            while q:
                i, j = q.popleft()
                for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < rows and 0 <= nj < cols and (ni,nj) not in visit \
                        and heights[ni][nj] >= heights[i][j]:
                        visit.add((ni,nj))
                        q.append((ni,nj))
            return visit

        pacific = [(0,c) for c in range(cols)] + [(r,0) for r in range(rows)]
        atlantic = [(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(rows)]

        return [[i,j] for i,j in bfs(pacific) & bfs(atlantic)]

