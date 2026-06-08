class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted([-s for s in stones])
        heapq.heapify(stones)

        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            new = abs(y - x)
            if x != y:
                heapq.heappush(stones, -new)
        return -stones[0] if len(stones) == 1 else 0