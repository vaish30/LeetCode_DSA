class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ele=min(nums)
        result=min_ele
        max_ele=max(nums)
        while result>0:
            if min_ele%result==0 and max_ele%result==0:
                break
            result-=1
        return result