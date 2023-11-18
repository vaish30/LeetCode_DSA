# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []

        while head:
            array.append(head.val)
            head = head.next
        print(array)
        l, r = 0, len(array) - 1
        print(l,r)
        while l <= r:
            if array[l] != array[r]:
                return False
            l += 1
            r -= 1
        return True

            
