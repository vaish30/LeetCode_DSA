# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        result = [sum(i) for i in zip(lst, lst[::-1])]
        return max(result)     