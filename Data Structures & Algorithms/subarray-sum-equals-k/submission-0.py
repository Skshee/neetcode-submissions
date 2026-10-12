class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        currSum = 0
        res = 0
        for num in nums:
            currSum += num

            if (currSum - k) in counts:
                res += counts[currSum - k]

            counts[currSum] = counts.get(currSum, 0) + 1
        return res
                