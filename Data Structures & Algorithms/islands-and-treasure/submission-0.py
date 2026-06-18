class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        def isValid(i, j):
            return 0<=i<m and 0<=j<n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    queue.append([i, j, 1])

        while queue:
            row, col, steps = queue.popleft()

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if (newRow, newCol) not in visited and isValid(newRow, newCol) and  grid[newRow][newCol] != -1:
                    visited.add((newRow, newCol))
                    grid[newRow][newCol] = steps
                    queue.append([newRow, newCol, steps + 1])


