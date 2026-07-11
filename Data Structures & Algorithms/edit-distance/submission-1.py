class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        from functools import cache
        @cache
        def dfs(w1, w2):
            if not w1 and not w2:
                return 0

            if w1 and w2 and w1[0] == w2[0]:
                return dfs(w1[1:], w2[1:]) # pop both without increment
            else:
                # delete character from w1
                del_ = ins = rep = float('inf')
                if w1:
                    del_ = dfs(w1[1:], w2)

                # insert character into w1 (prune w2 as matching)
                if w2:
                    ins = dfs(w1, w2[1:])

                # replace character in w1 (replace as matching)
                if w1 and w2:
                    rep = dfs(w1[1:], w2[1:])

                return min(del_, ins, rep) + 1

        return dfs(word1, word2)