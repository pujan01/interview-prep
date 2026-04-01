class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for index, value in enumerate(nums):
            if target - value in myMap:
                return [myMap[target - value], index]
            myMap[value] = index
            