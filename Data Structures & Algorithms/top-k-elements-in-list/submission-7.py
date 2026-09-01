class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        res = [[] for _ in range(n + 1)]
        ans = []
        counts = {}

        for i in range(n):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        for key, val in counts.items():
            res[val].append(key)

        for i in range(n, 0, -1):
            if res[i]:
                for num in res[i]:
                    ans.append(num)
                    k -= 1

                    if k == 0:
                        return ans

        return ans