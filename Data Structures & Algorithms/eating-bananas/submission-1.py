class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            hours = 0
            mid = (left + right)//2

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left