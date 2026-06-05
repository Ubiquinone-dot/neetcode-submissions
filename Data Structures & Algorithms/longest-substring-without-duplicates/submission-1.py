class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=1
        n = len(s)
        i = 0
        
        l = 0
        for idx, start in enumerate(s):
            # with this start
            while True:
                if l + idx >= n:
                    break
                sub = s[idx:idx+l]
                if len(set(s[idx:idx+l+1])) == l+1:
                    l+=1
                else:
                    break
        return l