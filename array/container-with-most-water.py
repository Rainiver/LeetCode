class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # cap = min(height[l], height[r])*(r-l)
        n = len(height)
        l, r = 0, n-1
        cap = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            cap = max(cap, min(height[l], height[r]) * (r - l))
        return cap
        