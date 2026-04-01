class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = []
        product = 1
        for num in nums:
            productList.append(product)
            product *= num

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            print(product)
            print(productList)
            productList[i] = productList[i] * product
            product = nums[i] * product
        return productList

