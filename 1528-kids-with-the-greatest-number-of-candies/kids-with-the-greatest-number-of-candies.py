class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for i in range(0,len(candies)):
            print(i)
            if candies[i] + extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)

        return output

        