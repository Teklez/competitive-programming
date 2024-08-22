# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        m, n = len(board), len(board[0])
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        queue = deque([[i, j]])
        board[i][j] = 'B'
        while queue:
            i, j = queue.popleft()
            count = 0
            for d in directions:
                nexti, nextj = i + d[0], j + d[1]
                if nexti >= 0 and nexti < m and nextj >= 0 and nextj < n: 
                    if board[nexti][nextj] == 'M':
                        count += 1 
            if count > 0:
                board[i][j] = str(count)
            else:
                for d in directions:
                    nexti, nextj = i + d[0], j + d[1]
                    if nexti >= 0 and nexti < m and nextj >= 0 and nextj < n and board[nexti][nextj] == 'E': 
                        board[nexti][nextj] = 'B'
                        queue.append([nexti, nextj])

        return board
        

