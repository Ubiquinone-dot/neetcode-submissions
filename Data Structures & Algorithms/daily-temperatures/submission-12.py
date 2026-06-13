class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # remove last element of the monotonic stack
                j = stack.pop(-1)
                res[j] = i - j
            stack.append(i)


        return res

        # res = []
        # n=len(temperatures)
        # idx = []
        # for i in range(n-1, -1, -1):
        #     a = False
        #     for j in idx[::-1]:
        #         # Decide whether to pop the index
        #         if temperatures[i] >= temperatures[j]:
        #             idx.remove(j)
        #         if temperatures[j] > temperatures[i] and not a:
        #             res.append(j - i)
        #             a=True
        #     if not a:
        #         res.append(0)
        #     idx.append(i)
        #     print(i, idx)
        # return res[::-1]
