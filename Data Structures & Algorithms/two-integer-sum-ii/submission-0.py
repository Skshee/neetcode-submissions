class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = defaultdict(int)

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if numDict[complement]:
                return [numDict[complement], i + 1]
            
            numDict[numbers[i]] = i+1
        
        return []