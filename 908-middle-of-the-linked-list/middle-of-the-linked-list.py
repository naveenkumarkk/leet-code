# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        listCount = 0
        current = head
        while current is not None:
            listCount+=1
            current = current.next

        currentList = head
        startPoint =  listCount/2
        currentIndex = 0
       
        while currentList is not None:
            if currentIndex >= startPoint:
                head = head.next
            currentList = currentList.next
            currentIndex+=1

        return head