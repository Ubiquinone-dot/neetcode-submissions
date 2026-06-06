class Solution:
    def isValid(self, s: str) -> bool:
        conjugate = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        conjugate_t = {v:k for k, v in conjugate.items()}

        # counts = {}
        # def tot(counts):
        #     return sum(list(counts.values()))

        stack = []
        for c in s:
            # If it's a closing paranthesis
            if c in conjugate_t:
                # ... and if the last element of the stack is the opening parenthesis 
                if stack and stack[-1] == conjugate_t[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Only add opening parentheses
                stack.append(c)
        # Good if stack is empty
        return True if not stack else False

        # seq=[]
        # for l in range(len(s)):
        #     n_opened={left: 0 for left in conjugate.keys()}
        #     is_valid=False
        #     for r in range(l, len(s)):

        #         # Open another one for the s[r]
        #         if s[r] in conjugate:
        #             n_opened[s[r]] = 1 + n_opened.get(s[r], 0)

        #         # Close the left bracket for this value
        #         if s[r] in conjugate.values():
                    
        #             # When bracket gets closed without ever being opened
        #             if conjugate_t[s[r]] not in n_opened:
        #                 return False
        #             n_opened[ conjugate_t[s[r]] ] -= 1

        #         # Break if right found and no opened brackets remain
        #         if s[l] in conjugate and conjugate[s[l]] == s[r] and sum(list(n_opened.values())) == 0:
        #             is_valid=True
        #             break
        #     print(is_valid, s, n_opened)
        #     if not is_valid:
        #         return False
        # return True
            