class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = nums[0]
        for num in nums:
            if count == 0 and num != res:
                res = num
                count += 1
            elif num == res:
                count += 1
            elif num!= res:
                count -= 1
        
        return res