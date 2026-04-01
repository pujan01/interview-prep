class Solution:
    def rob(self, nums: List[int]) -> int:
        # amt[i] = max(amt[i-3], amt[i-2]) + nums[i]
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], nums[1], nums[2]+nums[0])
        amt = [0] * n
        amt[0] = nums[0]
        amt[1] = nums[1]
        amt[2] = nums[2] + nums[0]
        maxAmt = max(amt[0], amt[1], amt[2]) 
        for i in range(3,n):
            amt[i] = max(amt[i-2], amt[i-3]) + nums[i]
            maxAmt = max(maxAmt, amt[i])
        return maxAmt

