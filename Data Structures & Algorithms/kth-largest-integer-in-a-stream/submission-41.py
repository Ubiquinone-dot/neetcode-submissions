class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minval = -float("infinity")
        self.stream = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        # Binary alg to find insertion point
        if val < self.minval:
            return self.stream[0]
        
        self.stream.append(val)
        self.stream = sorted(self.stream, reverse=True)
        return self.stream[self.k-1]

        # n = len(self.stream)
        # l, r = 0, n-1
        # while (r - l) > 0:
        #     m = (r - l + 1) // 2
        #     v = self.stream[m]
        #     if val > v:
        #         l = m
        #     elif val <= v:
        #         r = m
        #     print(l, r, m, self.stream, self.stream[m], val)
        #     break
        # return self.stream[self.k]


