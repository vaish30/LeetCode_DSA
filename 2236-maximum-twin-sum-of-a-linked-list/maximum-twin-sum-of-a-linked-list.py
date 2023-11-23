# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLen(self, head: Optional[ListNode]) -> int:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count 


    def pairSum(self, head: Optional[ListNode]) -> int:

        current = head
        n = self.getLen(current)

        values = []

        while current:
            values.append(current.val)
            current = current.next

        i, j = 0, n-1

        sum = 0
        # print(values)

        while i<j:
            print(values[i])
            sum = max(sum, values[i]+values[j])
            i += 1
            j -= 1

        return sum
        
        # sum = {}

        # for i in range(0,n//2):
        #     sum[i] = i + (n-1-i)
        #     print (sum)
        
        # if sum:
        #     return twin_sum = list(sum.values())
        # else:
        #     return 0

        
        # return max(twin_sum)




        