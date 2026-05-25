class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                totalProd *= num

        ans = []

        for num in nums:
            if zeroCount > 1:
                ans.append(0)
            elif zeroCount == 1:
                if num == 0:
                    ans.append(totalProd)
                else:
                    ans.append(0)
            else:
                ans.append(totalProd // num)

        return ans