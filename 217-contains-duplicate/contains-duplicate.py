class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #using hash set - which contains no duplicates 
        # arr = set()
        # for i in nums:
        #     if i in arr:
        #         return True 
        #     arr.add(i)
        # return False
        
        
        
        #using hash map
        # arr = {}
        # for i in nums:
        #     if i in arr :
        #         return True
        #     arr[i] = arr.get(i,0) + 1
        #     print(i, arr[i])
            
        # return False

        #using sorting for less time complexity
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False



        