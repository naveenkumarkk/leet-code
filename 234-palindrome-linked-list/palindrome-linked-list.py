# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Logic 1
        # data = ''
        # while head is not None:
        #     data = data + str(head.val)
        #     head = head.next
        
        # lenData = len(data) - 1
        # reversedData = ''
        # while lenData >= 0:
        #     reversedData = reversedData + str(data[lenData])
        #     lenData -=1
        # return data[::-1] == data

        # Logic 2
        turtle = rabbit = head
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
        
        prev = None
        while turtle:
            next_node = turtle.next
            turtle.next= prev
            prev = turtle
            turtle = next_node
        
        first_half,second_half = head,prev

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half =  first_half.next
            second_half = second_half.next

        return True

            