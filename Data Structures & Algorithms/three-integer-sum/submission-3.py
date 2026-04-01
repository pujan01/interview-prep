class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [3,0,-2,-1,1,2] sorting
        # [-2,-1,0,1,2,3]
        # [-4, -1, -1, 0, 1, 2] iterate... find target, if more than target, go left, if less , go right 
        sortedList = sorted(nums)
        res = set()
        for index, num1 in enumerate(sortedList): 
            if num1 > 0:
                break
            l, r = index + 1, len(nums) - 1
            target = - num1 
            while l < r: 
                if sortedList[l] + sortedList[r] == target: 
                    res.add((num1, sortedList[l], sortedList[r]))
                    l += 1
                    r -= 1
                elif sortedList[l] + sortedList[r] > target: 
                    # l += 1
                    r -= 1
                elif sortedList[l] + sortedList[r] < target: 
                    # r -= 1
                    l += 1
        return list(res)
                


        