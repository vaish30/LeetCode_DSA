class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1

        while i<j:
            current_h = min(height[i], height[j])
            current_w = (j-i)

            area = current_h * current_w

            max_area = max(max_area, area)

            if height[i]>height[j]:
                j-=1
            else:
                i+=1

        return max_area




''' max_area = 0

for i in range(0, len(height)):
    for j in range(i+1, len(height)):
        # area = height * width
        current_height = min(height[i], height[j])
        current_width = j - i
        area = current_height * current_width
        max_area = max(max_area, area)

return ( max_area)'''