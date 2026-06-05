class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def to_ana(a):
            d = {}
            for s in a:
                d[s] = 1 + d.get(s, 0)
            return d
        
        out_set = []
        ana = []
        for i, a in enumerate(strs):
            if i not in out_set:
                matches=[]
                for j, b in enumerate(strs):
                    if j not in out_set:
                        if to_ana(b) == to_ana(a):
                            matches.append(b)
                            out_set.append(j)
                ana.append(matches)


        return ana
