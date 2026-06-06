class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # When S1 cannot substring S2
        if len(s1) > len(s2):
            return False

        # ... initialize diff between s1 and s2 for the zeroth window
        diff = [0]*26
        for c in s1:
            diff[ord(c) - ord('a')] -= 1
        
        # Add the zeroth window to begin with
        for c in s2[:len(s1)]:
            diff[ord(c) - ord('a')] += 1

        # Base case where window already matches
        if sum([abs(a) for a in diff]) == 0:
            return True
    

        # Start loop from l=0, r=len(s1)
        l = 0
        for r in range(len(s1), len(s2)):

            # Add new char to window (appears so increment)
            diff[ ord(s2[r]) - ord('a') ] += 1

            # Slide one over (remove the increment that was placed before)
            diff[ ord(s2[l]) - ord('a') ] -= 1
            l += 1

            # if zero difference then exact match
            if sum([abs(a) for a in diff]) == 0:
                return True
        
        return False
                

        # # Create a count dict of s1
        # countS1 = {}
        # for c in s1:
        #     countS1[c] = 1 + countS1.get(c, 0)

        # # Slide window over s2, checking equivalence to s1
        # window = {}
        # l = 0
        # def is_match(window):
        #     return all([
        #         window.get(c, 0) == countS1.get(c, 0)
        #         for c in set(window.keys()) | set(countS1.keys())
        #     ])


        # def is_superset(window):
        #     return all([
        #         window.get(c, 0) >= countS1[c]
        #         for c in countS1
        #     ])
        # for r in range(len(s2)):

        #     # Increment window
        #     window[s2[r]] = 1 + window.get(s2[r], 0)
            
        #     # Check if the window contains a permutation of S1 as a substring
        
        #     if is_match(window):
        #         return True
            
        #     while is_superset(window) and sum(list(window.values())):
        #         # Slide window by one.
        #         window[s2[l]] -= 1
        #         l += 1
                
        #         # Check again if is match
        #         if is_match(window):
        #             return True

        return False