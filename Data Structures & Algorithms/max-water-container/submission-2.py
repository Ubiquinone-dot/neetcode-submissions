class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need largest difference in index * min(left, right) value
        n=len(heights)
        maxheight=0
        i=0
        j=n-1

        while j > i:
            height = min(heights[i], heights[j]) * abs(i - j)
            maxheight = max(height, maxheight)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxheight