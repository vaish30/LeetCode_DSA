# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head

        #this way we will find middle of the list(slow) and end of the list(fast)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reversing the second half of the linked list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev
        while right:
            if left.val !=right.val:
                return False
            
            #in ll u increment using .next 
            left = left.next 
            right = right.next
        return True




    def isPalindrome_usingArrayMethod(self, head: Optional[ListNode]) -> bool:
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

            
