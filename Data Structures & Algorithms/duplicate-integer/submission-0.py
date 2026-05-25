class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for i in range(len(nums)):
            if nums[i] not in sett:
                sett.add(nums[i])
            else:
                return True
        return False
        