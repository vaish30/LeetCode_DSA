# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 nums.remove(nums[i])
#                 nums.append(0) 
#             else:
#                 i+=1       

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Initialize two pointers
        left, right = 0, 0

        # Move non-zero elements to the left
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
