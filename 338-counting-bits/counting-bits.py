class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]
        
        # dp array and base cases
        dp_array = [0 for x in range(n + 1)]
        dp_array[1] = 1
        
        # iterate over the dp array
        for x in range(2, n + 1):
            
            # if a number is even, check the index in the 
            # dp array at index x//2, if uneven do the same but add one
            if x %2 == 0:
                dp_array[x] = dp_array[x//2]
            else:
                dp_array[x] = dp_array[x//2] + 1

        return dp_array 