class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0 # largest valid window seen
        windowSet = set() # sliding window set
        l=0 # pointer to the beginning of the window
        
        # loop through set once
        for i in range(len(s)):
            # If the window (l -> i) contains duplicates, remove them from the left
            # if the current character i is in the charset for the window, remove from left upward
            while s[i] in windowSet:
                windowSet.remove(s[l])
                l+=1
            
            # Add the new characer to the window
            windowSet.add(s[i])

            # Update the max window seen
            res = max(res, i - l + 1)

        return res