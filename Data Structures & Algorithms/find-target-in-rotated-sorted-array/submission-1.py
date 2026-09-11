class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # Then all elements from left to mid are sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # then all elements from mid to right are sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left

