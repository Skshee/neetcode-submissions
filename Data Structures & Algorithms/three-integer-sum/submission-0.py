class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                currsum = nums[i] + nums[left] + nums[right]

                if currsum == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    
                    # Move 'left' past any duplicates of the number just used.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Similarly for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif currsum < 0:
                    left += 1
                
                else:
                    right -= 1
            
        return ans
