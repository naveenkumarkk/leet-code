# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        position = 0
        dummyNode= ListNode(0)
        dummyNode.next = head
        fastNode = dummyNode
        slowNode = dummyNode

        for i in range(n+1): 
            fastNode = fastNode.next
        
        while fastNode is not None:
            fastNode =fastNode.next
            slowNode = slowNode.next
       
        slowNode.next = slowNode.next.next
            
        return dummyNode.next
        