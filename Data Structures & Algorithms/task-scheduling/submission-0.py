class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        counts = Counter(tasks)
        # Building the max heap
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # add 1 cuz the count values are -ve in maxheap
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


        