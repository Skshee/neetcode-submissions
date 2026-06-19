from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = len(grid)
        n = len(grid[0])

        fresh = 0
        time = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue and fresh > 0:

            for _ in range(len(queue)):   # process one minute
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if isValid(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        queue.append((newRow, newCol))

            time += 1

        return time if fresh == 0 else -1