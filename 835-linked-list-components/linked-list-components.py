# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        counter = 0
        checkValue = 0
        while head is not None:
            value = head.val
            head = head.next
            found = False
           
            for n in nums:
                if n == value:
                    checkValue +=1
                    found = True
                    break
            
            if found == False and checkValue > 0:
                checkValue = 0
                counter += 1
        
        if checkValue > 0:
            counter += 1
        
        return counter
            
            
                


