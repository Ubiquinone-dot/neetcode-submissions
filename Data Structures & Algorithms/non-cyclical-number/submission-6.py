class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while 1 not in seen:

            m = sum([int(a)**2 for a in str(n)])
            if m in seen:
                return False
            elif m == 1:
                return True

            seen = seen | {int(m)}
            n = m
            