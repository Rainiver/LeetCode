# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = []
        cur = head
        ans = 0
        while cur:
            res.append(cur.val)
            cur = cur.next
        n = len(res)
        for i in range(n-1, -1, -1):
            ans += res[i] * 2 ** (n-1-i)
        return ans

        