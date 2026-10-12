class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        l, r = 0, n-1

        while l < r:
            currHeight = min(heights[l], heights[r])
            currArea = currHeight * (r - l)
            maxArea = max(maxArea, currArea)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            
        return maxArea