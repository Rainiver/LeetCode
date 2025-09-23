# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        # 主要问题在于长度不一致不能同时移，需要把ab长度找出来，然后一个先移
        len_a, len_b = 0, 0
        while p1:
            len_a += 1
            p1 = p1.next
        while p2:
            len_b += 1
            p2 = p2.next
        p1, p2 = headA, headB
         
        while p1 and p2:
            if len_a > len_b:
                while len_a > len_b:
                    p1 = p1.next
                    len_a -= 1

            elif len_b > len_a:
                while len_b > len_a:
                    p2 = p2.next
                    len_b -= 1
            
            if p1 != p2:
                p1 = p1.next
                p2 = p2.next
            else:
                return p1
        
        return None
