class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        ans = -1
        n = len(nums)
        for i in range(1, n):
            min_val = min(min_val, nums[i-1])
            ans = max(nums[i] - min_val, ans)
        return ans if ans > 0 else -1
