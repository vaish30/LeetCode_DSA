class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # i = 0
        f= [0] + flowerbed + [0]
        for i in range(1,len(f)-1):
            # print(flowerbed[i-1])
            if (f[i] == 0) and f[i+1]==0 and (f[i-1]==0) :
                f[i] = 1 
                n-=1
 
        return n <= 0

            
        
            
            

            

        