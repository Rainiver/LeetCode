# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        pivot = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # 找到相遇点，退出循环
                pivot = slow
                break

        if pivot:
            # 一个从head，一个从pivot出发，最终相遇 
            slow = head
            fast = pivot
            while fast and slow:
                if fast == slow:
                    return slow
                fast = fast.next
                slow = slow.next

        return None