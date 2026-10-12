class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            time = 1
            mid = (left + right)//2
            currWeight = 0

            for i in range(len(weights)):
                if currWeight + weights[i] <= mid:
                    currWeight += weights[i]
                else:
                    time += 1
                    currWeight = weights[i]
            
            if time > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
                
            