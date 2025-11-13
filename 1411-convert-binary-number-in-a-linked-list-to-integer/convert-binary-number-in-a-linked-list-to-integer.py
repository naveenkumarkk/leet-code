# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_string = ''

        while head:
            binary_string += str(head.val)
            head = head.next
        return int(binary_string,2)
        