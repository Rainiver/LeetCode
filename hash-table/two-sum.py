class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 主要问题在于遇到2个相同的数字
        hashmap = {}
        n = len(nums)
        for i in range(n):
            if  nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if nums[i] * 2 == target:
                    return [i, hashmap[nums[i]]]
        
        for i in range(n):
            res = target - nums[i]
            if res in hashmap and res != nums[i]:
                return [i, hashmap[res]]
        