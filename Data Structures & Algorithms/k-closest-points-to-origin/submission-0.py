class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def reldist(p):
            return p[0]**2 + p[1]**2
        
        points = [(x, y, reldist([x, y])) for x, y in points]
        points = sorted(points, key=lambda x: x[-1])[:k]
        return [(x,y) for x,y,_ in points]
