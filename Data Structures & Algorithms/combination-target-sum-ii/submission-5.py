class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []

        def backtrack(start, curr, total):
            if total == target:
                ans.append(curr[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Early stopping
                if total + candidates[i] > target:
                    break

                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return ans