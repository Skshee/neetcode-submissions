class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        maxLength = 0

        for num in nums:
            if num-1 not in nums:
                numSet.add(num)
                length = 0
                while num + length in nums:
                    length += 1
                maxLength = max(length, maxLength)

        return maxLength