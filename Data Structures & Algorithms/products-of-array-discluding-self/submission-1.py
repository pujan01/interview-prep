class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = [1 for num in range(len(nums))]
        product = 1
        for index, num in enumerate(nums):
            productList[index] = product
            product *= num

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            productList[i] = productList[i] * product
            product = nums[i] * product
        return productList

