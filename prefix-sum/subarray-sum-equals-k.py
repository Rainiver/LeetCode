class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]*(n+1)
        
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i]+nums[i]

        count = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if k == prefix_sum[j] - prefix_sum[i]:
                    count += 1
        
        return count