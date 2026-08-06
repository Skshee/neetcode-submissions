class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in numDict:
                return [numDict[complement], i+1]
            
            numDict[numbers[i]] = i+1

        return [] 