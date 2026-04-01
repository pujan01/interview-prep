class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        movingSum = 0 
        l = 0 
        res = float("inf")
        for r in range(len(nums)):
            movingSum += nums[r]
            while movingSum >= target:
                res = min(res, r - l + 1)
                movingSum -= nums[l]
                l += 1 
        return res if res != float("inf") else 0
                 

