class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast, slow = 0, 0
        n = len(nums)
        while fast < n:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                slow = 0
                while fast != slow:
                    fast = nums[fast]
                    slow = nums[slow]
                return slow