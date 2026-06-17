class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        def dfs(i, j):
            currArea = 1

            for dr, dc in directions:
                newRow = i + dr
                newCol = j + dc

                if isValid(newRow, newCol) and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    currArea += dfs(newRow, newCol)
            return currArea

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    currArea = dfs(i, j)
                    maxArea = max(currArea, maxArea)
        return maxArea

        