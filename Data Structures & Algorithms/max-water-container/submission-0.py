class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need largest difference in index * min(left, right) value
        left=0
        right=1
        n=len(heights)
        maxheight=0
        for i in range(len(heights)):
            j=n-1
            while j > i:
                height = min(heights[i], heights[j]) * abs(i - j)
                maxheight = max(height, maxheight)
                j-=1
        return maxheight