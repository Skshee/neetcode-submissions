class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        leftProd = 1
        rightProd = 1

        for i in range(n):
            res[i] = leftProd
            leftProd *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= rightProd
            rightProd *= nums[i]

        return res