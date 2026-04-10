class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        if not nums:
            return []

        path = []
        res = []

        def backtrack(start, movingSum):
            if movingSum == target:
                res.append(path[:])
            if movingSum >= target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, movingSum + nums[i])
                path.pop()

            
        backtrack(0,0)
        return res
            

