class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def findWord(wor, i, j):
            if word == wor:
                return True
            if not(0 <= i < len(board)):
                return False
            if not(0 <= j < len(board[0])):
                return False
            if (i, j) in visited:
                return False
            
            if len(wor) > len(word):
                return False
            # if not word.startswith(wor):
            #     return False
            if board[i][j] != word[len(wor)]:
                return False
            visited.add((i, j))
            if findWord(wor + board[i][j], i + 1, j):return True
            if findWord(wor + board[i][j], i, j + 1):return True
            if findWord(wor + board[i][j], i - 1, j): return True
            if findWord(wor + board[i][j], i , j - 1): return True
            visited.remove((i,j))
            # if findWord(wor,i + 1, j): return True
            # if findWord(wor,i, j + 1): return True
            # if findWord(wor,i - 1, j): return True
            # if findWord(wor,i, j - 1): return True

            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                if findWord('', i, j):
                    return True
        
        return False










            

            


        


        