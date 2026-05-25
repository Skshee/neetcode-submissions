class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ans = []

        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic and dic[complement] != i:
                ans.append(i)
                ans.append(dic[target - nums[i]])
                break
        return ans
        