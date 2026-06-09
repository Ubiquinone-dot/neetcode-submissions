class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []            
        for i in range(n+1):
            resi = 0
            for j in range(32):
                new = i | 2**j
                if new == i:
                    resi+=1
            res.append(resi)

        return res