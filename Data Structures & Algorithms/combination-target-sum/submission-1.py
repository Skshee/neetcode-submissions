class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backTrack(start, curr, currSum):
            if currSum == target:
                ans.append(curr[:])
                return

            if currSum > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backTrack(i, curr, currSum + nums[i])
                curr.pop()
        
        backTrack(0, [], 0)
        return ans
