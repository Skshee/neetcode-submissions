class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = 1
        leftProd = 1

        res = []

        n = len(nums)

        for i in range(n):
            res.append(rightProd)
            rightProd *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] = res[i] * leftProd
            leftProd *= nums[i]
        
        return res
        