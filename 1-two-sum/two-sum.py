class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_a = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sum_a:
                return [sum_a[diff], i]

            sum_a[n] = i
            



    '''if len(nums) == 0:
            return False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]










       n_list = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j

        return False       '''