class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # nums[mid] could be the minimum
                right = mid

        return nums[left]