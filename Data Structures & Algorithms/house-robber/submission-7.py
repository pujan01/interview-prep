class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(n):
            if n == 0:
                return nums[n]
            if n == 1:
                return max(nums[0], nums[1])
            if n in memo:
                return memo[n]
            ans = max(helper(n-1), helper(n-2) + nums[n])
            memo[n] = ans
            return ans
        
        return helper(len(nums) - 1)
