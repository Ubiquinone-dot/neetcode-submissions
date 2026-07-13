class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        elif n == 2:
            return ['(())', '()()']
        # elif n == 3:
        #     return ['((()))', '(()())', '(())()', '()(())', '()()()']

        def dfs(n):
            if n == 1:
                return ['()']
            
            sub = dfs(n-1) 
            res = []
            n_bracket = len(sub[0]) // 2 + 1
            for i in range(len(sub)):
                for j in range(n_bracket):
                    brackets = sub[i] # str
                    brackets = brackets[:j] + "()" + brackets[j:]
                    if brackets not in res:
                        res.append(
                            brackets
                        )
                    # print(i, j, sub[i], res)

            return res

        return list(reversed(dfs(n)))