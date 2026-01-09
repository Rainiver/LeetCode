# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur, pre = head, None
        if left == right:
            return head

        for i in range(left-1):
            pre = cur
            cur = cur.next
        hl = pre
        end = cur

        for i in range(left, right+1):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        hl.next = pre
        end.next = cur
      
        return head
        