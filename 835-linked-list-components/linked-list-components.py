# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # Logic 1
        # counter = 0
        # checkValue = 0
        # while head is not None:
        #     value = head.val
        #     head = head.next
        #     found = False
           
        #     for n in nums:
        #         if n == value:
        #             checkValue +=1
        #             found = True
        #             break
            
        #     if found == False and checkValue > 0:
        #         checkValue = 0
        #         counter += 1
        
        # if checkValue > 0:
        #     counter += 1
        
        # return counter

        # Logic 2
        num_set = set(nums)
        counter = 0
        in_component = False

        while head:
            if head.val in num_set:
                if not in_component:
                    counter +=1
                    in_component = True
            else:
                in_component = False
            head = head.next
        return counter

            
            
                


