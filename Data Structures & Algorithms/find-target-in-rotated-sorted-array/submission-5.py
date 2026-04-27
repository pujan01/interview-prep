class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, hi = 0, len(nums) - 1
        while low <= hi:
            mid = low + (hi - low) // 2
            if nums[mid] == target:
                return mid 
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    low = mid + 1
                else:
                    hi = mid - 1 
        return -1
                    




