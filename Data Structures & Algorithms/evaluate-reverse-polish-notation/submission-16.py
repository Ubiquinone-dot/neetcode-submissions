class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[-1]
        
        # res = tokens.pop(0)
        # res = int(res)
        # OPS = ['*', '-', '+', '/']

        # while tokens:
        #     ops = []
        #     others = []
        #     print(tokens)
        #     while tokens and tokens[0] not in OPS:
        #         others.append(
        #             int(tokens.pop(0))
        #         )
        #     while tokens and tokens[0] in OPS:
        #         ops.append(
        #             tokens.pop(0)
        #         )
        #     print(ops, others)

        #     for other in others:
        #         for op in ops:
        # return res