# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head

        prev = None

        cur = ListNode()
        after = ListNode()
        cur = head

        while cur.next is not None:
            print(cur.val)
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        
        cur.next = prev

        return cur
            
        
