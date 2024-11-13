class Solution:

    def eff_containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)     
        
        return False

    def bad_containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]== nums[j]:
                    return True

        return False

    
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = nums.sort()

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False