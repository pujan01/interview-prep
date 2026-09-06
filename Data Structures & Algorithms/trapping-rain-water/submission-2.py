class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0 
        while l < r: 
            if maxL < maxR:
                l += 1
                res += max(min(maxL , maxR) - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                res += max(min(maxL , maxR) - height[r], 0)
                maxR = max(maxR, height[r])
        return res


            