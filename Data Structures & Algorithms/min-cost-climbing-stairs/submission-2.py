class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def helper(n):
            if n == 0 or n == 1:
                return 0
            if n in memo:
                return memo[n]
            ans = min(helper(n-1) + cost[n-1], helper(n-2)+cost[n-2])
            memo[n] = ans
            return ans 
        return helper(n)
        
                