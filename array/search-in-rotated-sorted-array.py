class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        # step 1: 寻找pivot，和右边界的数值比较
        while l< r:
            mid = (l + r) // 2
            if nums[mid] >  nums[r]:
                l = mid + 1
            else:
                r = mid
                
        pivot = l
        
        # 步骤2：确定目标所在的升序区间
        if target >= nums[0]:
            search_l, search_r = 0, pivot
        else:
            search_l, search_r = pivot, len(nums) - 1
        # step3: 普通区间用二分查找
        while search_l < search_r:
            mid = (search_l + search_r) // 2
            if nums[mid] < target:
                search_l = mid + 1
            else:
                search_r = mid
             
                
        return search_l if nums[search_l] == target else -1