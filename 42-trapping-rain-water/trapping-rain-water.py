class Solution:  
    def trap(self, height: List[int]) -> int:
        #at any given point max water which can be stored is potensial of water - height of the block, where as potential = min(max_left, max_right)

        left_wall = right_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i -1
            max_left[i] = left_wall
            max_right[j] = right_wall
            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])
        
        print(max_left)
        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])


        return summ


        
       