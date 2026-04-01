class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        if not nums:
            return []

        nums.sort()

        path = []
        res = []

        def backtrack(start, movingSum):
            if movingSum == target:
                res.append(path[:])
            if movingSum >= target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, movingSum + nums[i])
                path.pop()

            
        backtrack(0,0)
        return res
            
