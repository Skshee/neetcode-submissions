class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()

        for num in nums:
            if num not in sett:
                sett.add(num)
            else:
                return num
        
