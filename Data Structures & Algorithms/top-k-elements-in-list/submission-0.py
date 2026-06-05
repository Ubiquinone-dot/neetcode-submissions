class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {
            i: sum([int(i == x) for x in nums])
            for i in set(nums)
        }
        res = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = [r for r, _ in res]
        return res[:k]
            