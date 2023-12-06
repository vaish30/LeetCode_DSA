class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        postfix = 1
        prefix = 1
        for i in range (len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
        
              