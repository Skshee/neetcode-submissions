class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)

        for i, num in enumerate(nums):
            dic[num].append(i)
        
        for v in dic.values():
            if len(v) > 1:
                for i in range(1, len(v)):
                    if abs(v[i] - v[i-1]) <= k:
                        return True
        return False