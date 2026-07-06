class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for x, y in points:
            dist = (x**2 + y**2)**0.5
            heapq.heappush(heap, (dist,[x,y]))
        
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1

        return ans

