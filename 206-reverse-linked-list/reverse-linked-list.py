# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def insert_elements(self, val, next=None):
    #     new_node = ListNode(value, next=)
    #     head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #curr.next is a pointer so you have to break the pointer to next address and set the pointer to old address, let's say prev

        prev, curr = None, head
        
        if head == ' ':
            return []
        while curr:
            new_next = curr.next
            curr.next = prev
            prev = curr
            curr = new_next
        return prev


            


        # print(head)
        # print(new_head)
        