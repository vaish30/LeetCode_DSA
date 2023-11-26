class Solution:
    def getWinner_mine(self, arr: List[int], k: int) -> int:
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

    
    #implementing deque where we need quicker append and pop from the queue both the ends - functions used are append and popleft()

    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        one = q.popleft()

        x=k

        maximum = max(arr)

        if k>= len(arr):
            return maximum

        while k:
            two = q.popleft()
            if one > two:
                k -=1
                q.append(two)
            else:
                k=x
                k-=1
                q.append(one)
                one = two

        return one


                

        