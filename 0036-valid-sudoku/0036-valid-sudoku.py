from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        cells = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in columns[j]:
                    return False
                if board[i][j] in cells[(i//3, j//3)]:
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                cells[(i//3, j//3)].add(board[i][j])
        return True
