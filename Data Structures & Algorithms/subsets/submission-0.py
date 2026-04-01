class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def backtrack(index):
            if len(nums) == index:
                res.append(path[:])
                return
            
            # include 
            path.append(nums[index])
            backtrack(index+1)
            path.pop()

            # not include
            backtrack(index + 1)
        
        backtrack(0)
        return res 



            