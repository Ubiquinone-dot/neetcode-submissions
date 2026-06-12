class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Binary search over pile sizes O(log max(piles))
        l, r = 1, max(piles)
        res = float("inf")
        while r >= l:
            k = (r+l)//2

            # O(n)
            hrs = sum([
                (p//k + int(p % k > 0)) for p in piles
            ])

            if hrs > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

        return res
        # for k in range(1, 1000000):
        #     # Compute the number of hours to eat the bananas
        #     hrs = []
        #     for p in piles:
        #         # Number of hours to eat this pile = 1 + (p // k)
        #         hr = p//k + int(p % k > 0)
        #         hrs.append(hr)
        #     if sum(hrs) <= h:
        #         return k
        
        # piles = sorted(piles)
        # for k in range(1, 1000000):
        #     # Compute the number of hours to eat the bananas
        #     hrs = []
        #     for p in piles:
        #         # Number of hours to eat this pile = 1 + (p // k)
        #         hr = p//k + int(p % k > 0)
        #         hrs.append(hr)
        #     if sum(hrs) <= h:
        #         return k
        