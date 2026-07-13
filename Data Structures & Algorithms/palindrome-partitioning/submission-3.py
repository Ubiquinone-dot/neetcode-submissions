class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        res=[]
        stack=[]
        
        def dfs(i):
            if i == len(s):
                res.append(stack.copy())
                return

            stack.append(s[i])
            dfs(i+1) # you can always just pick the next character
            stack.pop()

            # check if the next character has a palindromic substring to make with the remainder.
            for j in range(i+1, len(s)):
                print(i,j)
                if s[i:j+1] == s[i:j+1][::-1]:
                    print(s[i:j+1], i,j)
                    stack.append(s[i:j+1])
                    dfs(j+1)
                    stack.pop()
            return
        dfs(0)
        return res