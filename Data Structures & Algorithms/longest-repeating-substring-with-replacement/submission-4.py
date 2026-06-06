class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n=len(s)
        counts = {}
        maxf = 0
        l = 0
        for i in range(n):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            maxf = max(maxf, counts[s[i]])
            
            # Slide the window
            while (i - l  + 1) > k + maxf:
                counts[s[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res