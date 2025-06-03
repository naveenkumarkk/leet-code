# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data = ''
        while head is not None:
            data = data + str(head.val)
            head = head.next
        
        # lenData = len(data) - 1
        # reversedData = ''
        # while lenData >= 0:
        #     reversedData = reversedData + str(data[lenData])
        #     lenData -=1
        return data[::-1] == data
            