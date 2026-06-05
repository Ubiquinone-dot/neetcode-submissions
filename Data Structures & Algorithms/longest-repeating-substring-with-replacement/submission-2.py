class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n=len(s)
        for i in range(n):
            counts, maxf = {}, 0
            for j in range(i, n):
                # increment count and find frequency of largest
                counts[s[j]] = 1 + counts.get(s[j], 0)
                maxf = max(maxf, counts[s[j]])
                if (j - i + 1) <= k + maxf:
                    res = max(res, j-i + 1)
        return res
