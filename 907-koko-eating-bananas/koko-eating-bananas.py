class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)

        total = sum(piles)
        min_r = total//h
        max_r = max(piles)

        l, r = 1, max_r
        print(l,r)


        while l<r:
            m = (l + r)//2
            if self.time_taken(piles,m) <= h:
                r=m
            else:    
                l=m+1
        
        return l
        

        

    def time_taken(self, piles, k):
        total_hours = 0
        for i in range(len(piles)):
            total_hours += math.ceil(piles[i]/k)

        return total_hours
            
            

        