class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        leftmost, rightmost = 1, 1

        size = len(nums)-1
        for i in range(len(nums)):
            j = size-i
            prefix[i] = leftmost
            postfix[j] = rightmost
            leftmost *= nums[i]
            rightmost *= nums[j]

        return [l*r for l,r in zip(prefix, postfix) ]

            






        '''output = [0]*len(nums)

        
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                temp = temp*nums[j]
              

            output[i]=temp
         
        
    
            

        print(output)

        return output
        '''