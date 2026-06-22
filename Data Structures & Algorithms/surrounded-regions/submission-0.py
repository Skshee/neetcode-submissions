class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Question is to be solved in 3 parts
        m = len(board)
        n = len(board[0])
        def dfs(r, c):
            if (r < 0 or c < 0 or r == m or c == n or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # 1 - (DFS) For unsurrounded regions,  convert "O" -> "T"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in [0, m-1] or j in [0, n-1]):
                    dfs(i, j)

        # 2 - For surrounded regions, convert "O" -> "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # 3 - Convert the "T" back to "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'