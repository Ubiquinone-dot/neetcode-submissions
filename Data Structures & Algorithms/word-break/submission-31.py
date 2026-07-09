

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = sorted(wordDict, reverse=True, key=lambda x : len(x))
        invalid = {}
        def dfs(i):
            srem = s[i:]
            if srem == '' or not srem:
                return True

            for w in wordDict:
                if srem.startswith(w):
                    if invalid.get(i, False):
                        return False
                    elif dfs(i+len(w)):
                        return True
            invalid[i] = True
            return False

        res = dfs(0)
        print(invalid)
        return res
        # dp = [s for _ in wordDict]
        # for i in wordDict:
        #     dp[i] = s.replace(wordDict[i], '')

        # print(dp)

        # srem = s
        # while srem:
        #     for w in wordDict:
        #         if srem.startswith(w):
        #             srem = srem.lstrip(w)
        #             print(srem)
        #             break
        #     else:
        #         return False
        # return True
