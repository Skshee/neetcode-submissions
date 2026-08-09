class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)   # ✅ initialize properly
        maxLength = 0

        for num in numSet:   # iterate over set
            if num - 1 not in numSet:   # ✅ check in set
                length = 0
                while num + length in numSet:  # ✅ check in set
                    length += 1
                maxLength = max(length, maxLength)

        return maxLength