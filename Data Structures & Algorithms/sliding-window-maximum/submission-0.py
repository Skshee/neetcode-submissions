class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        ans = []
        n = len(nums)

        currWindow = []
        for right in range(k):
            currWindow.append(nums[right])
        ans.append(max(currWindow))

        for right in range(k, n):
            currWindow.append(nums[right])
            currWindow.pop(0)
            ans.append(max(currWindow))
        return ans