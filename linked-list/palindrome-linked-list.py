# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 最大的问题是链表不能从后往前遍历，只能翻转链表然后比较，如果整条链表翻转然后和原链表比较则空间不是O(1)，因此只能翻转一半的链表然后比较一半，则不占用额外空间。
        # 快慢指针找中间点
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 此时s对应另一半的开始，翻转后一半链表
        mid = slow
        pre = None
        while slow:
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        
        # 比较2侧的链表
        p1, p2 = head, pre
        while p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True
        