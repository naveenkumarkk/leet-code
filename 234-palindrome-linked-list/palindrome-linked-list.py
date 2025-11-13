import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow =fast= head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        left,right = head,prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True