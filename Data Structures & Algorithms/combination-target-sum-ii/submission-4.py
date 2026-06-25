class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        dic = defaultdict(int)
        candidates.sort()

        for num in candidates:
            dic[num] += 1

        def backTrack(start,curr, total):
            if total == target:
                if curr not in ans:
                    ans.append(curr[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if dic[candidates[i]] > 0:
                    dic[candidates[i]] -= 1
                    curr.append(candidates[i])
                    total += candidates[i]
                    backTrack(i+1, curr, total)
                    total -= candidates[i]
                    curr.pop()
                    dic[candidates[i]] += 1
        
        backTrack(0, [], 0)
        return ans
        


            