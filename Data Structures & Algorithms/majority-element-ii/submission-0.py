class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        res = []

        for k,v in counts.items():
            if v > n/3:
                res.append(k)
        return res
        