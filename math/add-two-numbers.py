# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        result = ListNode()
        cur = result
        
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            val = val1 + val2 + carry
            cur.next = ListNode(val%10) 
            carry = val // 10
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            cur = cur.next

        # 补充：处理最终剩余的进位（若进位不为 0，新增节点）
        if carry > 0:
            cur.next = ListNode(carry)
            
        return result.next
            

        