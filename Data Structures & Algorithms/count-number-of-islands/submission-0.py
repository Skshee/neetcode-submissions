class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        m = len(grid) # Rows
        n = len(grid[0]) # Columns

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n 

        def dfs(i, j):
            for dr, dc in directions:
                newRow = i + dr
                newCol = j + dc

                if isValid(newRow, newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] == '1':
                    visited.add((newRow, newCol))
                    dfs(newRow, newCol)

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    numIslands += 1
                    visited.add((i, j))
                    dfs(i, j)
        return numIslands