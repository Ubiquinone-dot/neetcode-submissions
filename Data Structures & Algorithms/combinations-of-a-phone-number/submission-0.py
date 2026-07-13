class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_let = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return num_to_let[digits]

        start, end = digits[0], digits[1:]

        res = self.letterCombinations(end)
        ret = []
        for s in res:
            for s2 in num_to_let[start]:
                ret.append(
                    s2 + s
                )
        return ret