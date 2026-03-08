class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)


        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue
                
                if (value in row[r] or
                 value in col[c] or
                 value in square[(r//3,c//3)]
                 ):
                    return False
                row[r].add(value)
                col[c].add(value)
                square[(r//3,c//3)].add(value)

        return True


