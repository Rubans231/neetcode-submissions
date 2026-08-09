class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        
        while l < r:
            h_l, h_r = heights[l], heights[r]

            if heights[l] < heights[r]:
                area = h_l * (r - l)
                while l < r and heights[l] <= h_l:
                    l += 1
            else:
                area = h_r * (r - l)
                while l < r and heights[r] <= h_r:
                    r -= 1
            
            if area > max_area:
                max_area = area
                
        return max_area