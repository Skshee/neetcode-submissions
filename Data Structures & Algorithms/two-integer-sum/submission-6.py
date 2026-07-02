class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            print(complement)
            if complement in nums and i != dic[complement]:
                return [i, dic[complement]]
        