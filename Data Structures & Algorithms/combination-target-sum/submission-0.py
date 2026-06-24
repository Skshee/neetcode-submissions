class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backTrack(start, curr, total):
            if total == target:
                ans.append(curr[:])
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backTrack(i, curr, total + nums[i])
                curr.pop()

        backTrack(0, [], 0)
        return ans