class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen1 = set()
            seen2 = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen1:
                        return False
                    seen1.add(board[i][j])
                if board[j][i] != '.':
                    if  board[j][i] in seen2:
                        return False
                    seen2.add(board[j][i])

        for j in range(0, 7, 3):
            for k in range(0, 7, 3):
                seen = set()
                for i in range(j, j + 3):
                    for n in range(k, k + 3):
                        if board[i][n] != '.':
                            if board[i][n] in seen:
                                return False
                            seen.add(board[i][n])
        return True


        

        




        