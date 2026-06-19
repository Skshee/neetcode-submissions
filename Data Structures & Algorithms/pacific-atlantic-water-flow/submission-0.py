class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]

        for i in range(m):
            p_queue.append([i, 0])
            p_seen.add((i, 0))

        for j in range(1, n):
            p_queue.append([0, j])
            p_seen.add((0, j))

        for i in range(m):
            a_queue.append([i, n-1])
            a_seen.add((i, n-1))

        for j in range(n):
            a_queue.append([m-1, j])
            a_seen.add((m-1, j))

        def isValid(i, j):
            return 0<=i<m and 0<=j<n

        def getCoords(queue, seen):
            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if(newRow, newCol) not in seen and isValid(newRow, newCol) and heights[newRow][newCol] >= heights[row][col]:
                        seen.add((newRow, newCol))
                        queue.append([newRow, newCol])

        getCoords(p_queue, p_seen)
        getCoords(a_queue, a_seen)
        return list(p_seen.intersection(a_seen))
