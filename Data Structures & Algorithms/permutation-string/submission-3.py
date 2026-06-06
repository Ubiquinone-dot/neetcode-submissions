class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        # Create a count dict of s1
        countS1 = {}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)

        # Slide window over s2, checking equivalence to s1
        window = {}
        l = 0
        for r in range(len(s2)):

            # Increment window
            window[s2[r]] = 1 + window.get(s2[r], 0)
            
            def is_match(window):
                return all([
                    window.get(c, 0) == countS1.get(c, 0)
                    for c in set(window.keys()) | set(countS1.keys())
                ])


            def is_superset(window):
                return all([
                    window.get(c, 0) >= countS1[c]
                    for c in countS1
                ])
            # Check if the window contains a permutation of S1 as a substring
        
            if is_match(window):
                return True
            
            while is_superset(window) and sum(list(window.values())):
                # Slide window by one.
                window[s2[l]] -= 1
                l += 1
                
                # Check again if is match
                if is_match(window):
                    return True

        return False