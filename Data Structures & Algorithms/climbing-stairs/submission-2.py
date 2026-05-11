class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n == 1 or n == 2:
                return n 
            if n in memo:
                return memo[n]
            ans = helper(n-1) + helper(n-2)
            memo[n] = ans
            return ans
        return helper(n)