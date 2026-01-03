class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')  
        l = 0  
        current_sum = 0  
        
        for r in range(n):
            current_sum += nums[r]
            
            while current_sum >= target:
                min_len = min(min_len, r - l + 1)
                current_sum -= nums[l]
                l += 1
        
        return min_len if min_len != float('inf') else 0
        