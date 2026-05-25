class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSet = [set() for _ in range(9)]
        rowSet = [set() for _ in range(9)]
        subboxSet = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in rowSet[i] and board[i][j] not in colSet[j] and board[i][j] not in subboxSet[i//3][j//3]:
                    rowSet[i].add(board[i][j])
                    colSet[j].add(board[i][j])
                    subboxSet[i//3][j//3].add(board[i][j])
                else:
                    return False
        return True