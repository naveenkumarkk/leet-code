class Node:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operation_count = 0
        dummy = Node()
        current = dummy

        for val in nums:
            current.next = Node(val)
            current = current.next

        head = dummy.next

        while head:
            is_sorted = True
            curr = head

            while curr and curr.next:
                if curr.val > curr.next.val:
                    is_sorted = False
                    break
                curr = curr.next
            
            if is_sorted:
                break
            
            operation_count += 1

            minimum_sum = float('inf')
            minimum_node = None
            curr = head
            while curr and curr.next:
                node_sum = curr.val + curr.next.val
                if node_sum < minimum_sum:
                    minimum_sum = node_sum
                    minimum_node = curr
                curr = curr.next
            
            if minimum_node:
                minimum_node.val = minimum_sum
                node_to_remove = minimum_node.next
                minimum_node.next = node_to_remove.next
            else:
                break

        return operation_count
