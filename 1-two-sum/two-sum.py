#brute force method 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    output = i,j

        return output
                    

# #hash table method 
#     def twoSum(self,num: List[int], target: int) -> List[int]:
#         table = {}

#         # for i in range(len(num)):
#         #     complement = target - num[i]

#         #     if complement in table:
#         #         return [table[complement],i]
            
#         #     table[num[i]] = i
#         #     print(num[i],i)

#         # return []


        