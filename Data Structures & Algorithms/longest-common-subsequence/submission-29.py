class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

        # dp = {}

        # def search(i,j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if (i,j ) in dp:
        #         return dp[(i,j)]

        #     if text1[i] == text2[j]:
        #         dp[(i,j)] = max(dp.get((i,j), 0), search(i+1, j+1) + 1)
        #         return dp[(i, j)]
        #     else:
        #         l = search(i+1, j)
        #         r = search(i, j+1)
        #         dp[(i,j)] = max(l, r, dp.get((i,j), 0))
        #         return max(l, r)

        # v = search(0, 0)
        # print(dp, v)
        # return dp[(0,0)]
        # hitsj = set()
        # hitsi = set()
        # for i in range(len(text1)):
        #     for j in range(len(text2)):
        #         same = int(text1[i] == text2[j])
        #         maxx = max(dp.get((i-1, j), 0), dp.get((i, j-1), 0))
        #         if i not in hitsi and j not in hitsj:
        #             dp[(i, j)] = same + maxx
        #             if same:
        #                 hitsi, hitsj = hitsi | {i}, hitsj | {j}
                
        # print(dp)
        # return dp.get((i,j), 0)
        # def dfs(i, j):
            
        #     if text1[i] == text2[j]:
        #         dp[(i,j)] = 1
        #         dfs(i+1, j+1)
        #     else:
        #         # Try both
        #         dfs(i+1, j)
        #         dfs(i, j+1)
        
        # dfs(0,0)