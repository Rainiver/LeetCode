class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # 二分查找，直到left == right
        while left < right:
            mid = (left + right) // 2
            # 比较mid和mid+1，缩小范围
            if nums[mid] > nums[mid + 1]:
                # 峰值在左半区（包括mid）
                right = mid
            else:
                # 峰值在右半区（mid+1及右侧）
                left = mid + 1
        
        # 最终left==right，就是峰值索引
        return left
        
        