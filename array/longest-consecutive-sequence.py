class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in num_set:
                cur = 0
                while num in num_set:
                    cur += 1
                    num += 1
                ans = max(ans, cur)
            else:
                continue
        return ans

        