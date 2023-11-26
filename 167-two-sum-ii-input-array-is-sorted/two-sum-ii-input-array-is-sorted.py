class Solution:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
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



    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1


            