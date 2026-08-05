class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        subBoxSet = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in rowSet[i] and board[i][j] not in colSet[j] and board[i][j] not in subBoxSet[i//3][j//3]:
                    rowSet[i].add(board[i][j])
                    colSet[j].add(board[i][j])
                    subBoxSet[i//3][j//3].add(board[i][j])
                else:
                    return False
        return True
