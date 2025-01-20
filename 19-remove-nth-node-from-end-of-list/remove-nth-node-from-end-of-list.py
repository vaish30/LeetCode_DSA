# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev = None
        curr = head 
        while curr:
            nxt = curr.next
            curr.next = rev
            rev = curr
            curr = nxt
        # print(rev)

        dummy = ListNode()
        dummy.next = rev
        prev = dummy
        hops = 0
        while prev:
            hops+=1
            if hops == n:
                prev.next = prev.next.next
                break
            prev = prev.next

        print(prev)
        inital = None
        final = dummy.next
        while final:
            nxt = final.next
            final.next = inital
            inital = final
            final = nxt

        return inital


