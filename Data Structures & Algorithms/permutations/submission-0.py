class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        path = []
        picks = [False] * len(nums)
        
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if picks[i]:
                    continue
                picks[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                picks[i] = False

        backtrack()
        return res