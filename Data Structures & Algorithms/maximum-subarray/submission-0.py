class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if curSum < 0:
                curSum = 0
            curSum = num + curSum 
            if curSum < 0:
                curSum = num
            maxSum = max(maxSum, curSum)
        return maxSum