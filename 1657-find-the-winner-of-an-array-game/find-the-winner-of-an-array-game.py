class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0],arr[1])
        if k >=len(arr):
            return max(arr)

        winner = arr[0]
        count = 0
        for i in range(1,len(arr)) :
            if winner > arr[i]:
                count +=1
            else: 
                winner = arr[i]
                count = 1

            if count == k:
                return winner

        return winner

                

        