# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            # If pointerA reaches the end of list A, move it to the head of list B
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next

            # If pointerB reaches the end of list B, move it to the head of list A
            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next

        return pointerA

        

    
        