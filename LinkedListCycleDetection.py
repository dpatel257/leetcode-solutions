# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        singleP = head
        halfP = head
        tiktok = True
        while singleP.next:
            print("SingleP:", singleP.val)
            singleP = singleP.next
            tiktok = not tiktok

            if tiktok:
                halfP = halfP.next
          

            if singleP == halfP:
                return True       
        
        return False
