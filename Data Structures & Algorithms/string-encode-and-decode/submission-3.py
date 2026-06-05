class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(strs) + '|' + ','.join([
            str(len(s)) for s in strs])

    def decode(self, s: str) -> List[str]:
        msg, key = '|'.join(s.split('|')[:-1]), s.split('|')[-1]
        res = []
        idx=0
        if not key:
            return []
        for l in key.split(','):
            l = int(l)
            res.append(
                msg[idx:l+idx]
            )
            idx+=l
        return res