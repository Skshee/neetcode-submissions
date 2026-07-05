class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        n = len(nums)

        for i in range(n-k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
        