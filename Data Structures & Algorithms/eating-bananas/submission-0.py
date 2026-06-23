class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeTaken(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            return time

        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            if timeTaken(mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        
        