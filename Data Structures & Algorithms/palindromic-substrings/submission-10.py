class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n=len(s)

        for i in range(len(s)):
            l = r = i 
            
            # Search even
            while r < n and l >= 0 and  s[l] == s[r]:
                res+=1
                l, r = l-1, r+1
        
            # search odd
            l, r = i, i+1
            while r < n and l >= 0 and s[l] == s[r]:
                res += 1
                l, r = l-1, r+1

            # l = i
            # r = len(s) - 1
            # for r in range(l, len(s)+1):
            #     if l == r:
            #         continue
            #     if s[l:r] == s[l:r][::-1]:
            #         res+=1
        return res