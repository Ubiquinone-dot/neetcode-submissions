class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}

        for l in s:
            ds[l] = 1 + ds.get(l, 0)
        for l in t:
            dt[l] = 1 + dt.get(l, 0)
        
        return ds == dt
