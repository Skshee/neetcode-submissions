class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()

        def dfs(i, j, index):
            # Entire word has been matched
            if index == len(word):
                return True

            # Out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            # Cell already used in this path
            if (i, j) in path:
                return False

            # Character doesn't match
            if board[i][j] != word[index]:
                return False

            # Mark current cell as visited
            path.add((i, j))

            # Explore all 4 directions
            res = (
                dfs(i + 1, j, index + 1) or
                dfs(i - 1, j, index + 1) or
                dfs(i, j + 1, index + 1) or
                dfs(i, j - 1, index + 1)
            )

            # Backtrack
            path.remove((i, j))

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False