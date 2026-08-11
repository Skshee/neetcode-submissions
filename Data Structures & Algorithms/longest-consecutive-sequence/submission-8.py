from sortedcontainers import SortedSet

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = SortedSet(nums)

        longest = 0
        curr = 0

        for num in s:
            if num - 1 not in s:
                curr = 1
            else:
                curr += 1

            longest = max(longest, curr)

        return longest