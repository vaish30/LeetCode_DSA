# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None
        while current:
            tmp =  current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

    #recursion gives us the way to traverse the list in forward direction first and then in the backward direction
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if head is None or head.next is None:
            return head

        current = head

        #exit condition for recursive calls
        if (current.next == None):
            head = current
            return current

        rec_rev = self.reverseList(current.next)
        temp = current.next
        temp.next = current
        current.next = None        

        return rec_rev
        


         


        