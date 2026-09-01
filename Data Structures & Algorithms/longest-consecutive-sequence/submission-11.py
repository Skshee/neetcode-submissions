class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        longest = 0
        curr = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if i > 0 and nums[i] == nums[i - 1] + 1:
                curr += 1
            else:
                curr = 1

            longest = max(longest, curr)

        return longest