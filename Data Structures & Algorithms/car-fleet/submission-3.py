class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        idx = sorted([
            (i, position[i], speed[i]) for i in range(len(position))
        ], key = lambda x: x[1], reverse=True)
        stack = []
        for i, p, s in idx:
            t = (target - p) / s
            for (j, t2) in stack:
                if t <= t2:
                    break
            else:
                stack.append((i, t))
        return len(stack)