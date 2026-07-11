class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = 1
        currMin = 1

        for num in nums:
            temp = currMax * num

            currMax = max(num, temp, num * currMin)
            currMin = min(num, temp, num * currMin) # Use temp because we need the currMax of previous iteration not of the current one we just found
            res = max(res, currMax)
        
        return res