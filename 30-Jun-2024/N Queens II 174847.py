# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pDiag = set()
        nDiag = set()
        res = 0
        board = [["." for i in range(n)] for i in range(n)]

        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            for c in range(n):
                if c in cols or (row + c) in pDiag or (row - c) in nDiag:
                    continue
                cols.add(c)
                pDiag.add(row + c)
                nDiag.add(row - c)
                board[row][c] = "Q"

                backtrack(row + 1)

                cols.remove(c)
                pDiag.remove(row + c)
                nDiag.remove(row - c)
                board[row][c] = "."
        backtrack(0)
        return res
        



