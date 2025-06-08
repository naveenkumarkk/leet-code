# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        current = self.head
        choosen_value = current.val
        count = 1

        while current:
            if random.randint(1,count) == 1:
                choosen_value = current.val
            current = current.next
            count+=1
        return choosen_value
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()