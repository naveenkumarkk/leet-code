# Definition for singly-linked list.
class ListNode:
    def __init__(self,value):
        self.data = value
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        self.head = head
        if (self.head is None):
            return False
        else:  
            current_node = self.head
            fastNode = current_node
            while(current_node.next is not None and fastNode.next is not None and fastNode.next.next is not None):
                current_node = current_node.next
                fastNode = fastNode.next.next
                if(current_node == fastNode):
                    return True
                
        return False
            
        
        