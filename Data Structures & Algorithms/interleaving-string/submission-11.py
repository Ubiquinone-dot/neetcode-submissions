class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        from functools import cache
        if len(s1+s2) != len(s3):
            return False
        @cache
        def dfs(i, j):
            if i > len(s1) - 1:
                print('ll')
                return s2[j:] == s3[j+i:]
            elif j > len(s2) - 1:
                print('dd')
                return s1[i:] == s3[j+i:]

            if i == len(s1) - 1 and j == len(s2) - 1:
                print('Tru')
                return True

            left=right=False
            # print(s1[i], s1[i:], s2[j], s2[j:], '->', s3[i+j], s3[j+i:], i, j)
            if s1[i] == s3[i+j]:
                left = dfs(i+1, j)
            if s2[j] == s3[i+j]:
                right = dfs(i, j+1)
            return left or right

        return dfs(0, 0)