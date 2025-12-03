class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        prefix = 0
        pre_map = {0: 1}
        for i in range(n):
            prefix += nums[i]
            if prefix not in pre_map:
                pre_map[prefix] = 1
            else:
                pre_map[prefix] += 1
            target = prefix - k
            if target in pre_map:
                ans += pre_map[target]
        return ans
        