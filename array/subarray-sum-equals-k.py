class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_sum = 0
        pre_dict = {0:1}        
        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_dict:
                count += pre_dict[pre_sum - k]
            if pre_sum in pre_dict:
                pre_dict[pre_sum] += 1
            else:
                pre_dict[pre_sum] = 1
        
        return count