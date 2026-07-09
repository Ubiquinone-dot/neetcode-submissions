class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        res = ""
        for l in range(len(s)):
            r = len(s)
            # print(s[l:r], 'then', (s[l:r:])[::-1])
            while l < r and r - l > len(res):
                if s[l:r] == s[l:r][::-1]:
                    res = s[l:r]
                r-=1
        return res

