class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        countT, window = {}, {}

        # collect T counts
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        resLen = float("infinity")
        res = [0, len(s)-1]

        # Slide a window from left to right
        l=0
        for r in range(len(s)):
            # Fetch right-most character added to the window
            c = s[r]

            # Increment window counter for current character
            window[c] = 1 + window.get(c, 0)

            # if c in countT and window[c] == countT[c]:
            #     # New character count matches target exactly
            #     # have is the max of 
            #     have += 1
            
            # Compare window and target 
            def contains(window, countT):
                return all([
                    countT[c] <= window.get(c,0) for c in countT
                ])

            # while our window contains the string, reduce the window size
            while contains(window, countT):
                # Update result and result length if current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Reduce window from left
                window[s[l]] -= 1
                l+=1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

