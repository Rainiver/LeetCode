# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        lh, rh = ListNode(0), ListNode(0)
        l, r = lh, rh
        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                r.next = cur
                r = r.next
            cur = cur.next
        r.next = None
        l.next = rh.next
        return lh.next
