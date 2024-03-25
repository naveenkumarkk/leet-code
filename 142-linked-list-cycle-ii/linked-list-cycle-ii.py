# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hasCycle = False
        if(head is None):
            return None
        else:
            current_node = head
            fast_node = head
            while(current_node.next is not None and  fast_node.next is not None and fast_node.next.next is not None):
                current_node = current_node.next
                fast_node = fast_node.next.next
                if(current_node == fast_node):
                    hasCycle = True
                    break
                
            if(hasCycle):
                current_node = head
                while current_node != fast_node:
                    current_node = current_node.next
                    fast_node = fast_node.next
                return current_node

        return None