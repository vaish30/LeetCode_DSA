# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()  # Sort the array.

#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue  # Skip duplicates.

#             target = -nums[i]
#             left, right = i + 1, len(nums) - 1

#             while left < right:
#                 current_sum = nums[left] + nums[right]

#                 if current_sum == target:
#                     result.append([nums[i], nums[left], nums[right]])
#                     left += 1
#                     right -= 1

#                     # Skip duplicates.
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1

#                 elif current_sum < target:
#                     left += 1
#                 else:
#                     right -= 1

#         return result



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        target = 0

        nums.sort()
        # j=i+1
        # k=len(nums)-1 


        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    k-=1

        return list(result)
                    





        

        