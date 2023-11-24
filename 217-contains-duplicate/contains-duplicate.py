class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #using hash set - which contains no duplicates 
        arr = set()
        for i in nums:
            if i in arr:
                return True 
            arr.add(i)
        return False
        
        
        
        #using hash map
        # arr = {}
        # for i in nums:
        #     if i in arr :
        #         return True
        #     arr[i] = arr.get(i,0) + 1
        #     print(i, arr[i])
            
        # return False



        