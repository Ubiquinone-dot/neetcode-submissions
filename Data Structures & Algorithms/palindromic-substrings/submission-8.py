class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for l in range(len(s)):
            r = len(s) - 1
            for r in range(l, len(s)+1):
                if l == r:
                    continue
                if s[l:r] == s[l:r][::-1]:
                    res+=1
        return res