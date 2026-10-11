class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [[] for _ in range(n+1)]
        ans = []
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        

        for num, freq  in counts.items():
            res[freq].append(num)
        
        for i in range(n, -1, -1):
            if k == 0:
                break
            else:
                if res[i]:
                    for val in res[i]:
                        ans.append(val)
                        k -= 1
        return ans
