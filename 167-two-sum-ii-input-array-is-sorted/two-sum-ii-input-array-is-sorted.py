class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []

        left, right = 0, len(numbers)-1

        while left<right:
            # mid = left + (right - left) // 2

            sum = numbers[right]+numbers[left]  

            if sum == target:
                output.append(left+1)
                output.append(right+1)
                return output
            
            
            elif sum < target:
                left = left+1
            
            else:
                right = right-1

        return output






        