class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        numSet = set(nums)
        counts = 1
        res = 1
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                counts = 1
                number = nums[i]
                while number + 1 in numSet:
                    number += 1
                    counts += 1
                    res = max(counts, res)
                    
        return res