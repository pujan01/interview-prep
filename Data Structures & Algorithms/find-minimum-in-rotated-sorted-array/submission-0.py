class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        res = nums[0]
        while l <= h:
            mid = (l + h) // 2
            if nums[l] <= nums[h]:
                res = min(res, nums[l])
                break
            res = min(res, nums[mid])
            if nums[mid] > nums[h]:
                l = mid + 1                
            else:
                h = mid - 1

        return res
