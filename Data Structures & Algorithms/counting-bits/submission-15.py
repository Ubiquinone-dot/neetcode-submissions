class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = [0, 1]
        offset=0
        for i in range(2, n+1):
            phi = i & (i - 1)
            if phi==0:
                res.append(1)
                offset=i
            else:
                nres = 1 + res[i - offset]
                res.append(nres)
        return res