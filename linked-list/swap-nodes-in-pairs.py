# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (not head.next):
            return head
        
        
        dummy = ListNode(next=head)
        cur = dummy
       
        """
        tmp2 = 3
        cur  tmp1     tmp2   
        0 -> 1 -> 2 -> 3 -> 4
            pre  cur
        0 -> 2 -> 1 -> 3
        1->
        """
        while cur.next and cur.next.next:
            tmp2 = cur.next.next.next
            tmp1 = cur.next
            cur.next = cur.next.next
            cur.next.next = tmp1
            tmp1.next = tmp2
            
            cur = cur.next.next
        
        return dummy.next
        