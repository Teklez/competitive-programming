class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        dir = 0
        n = len(mat)

        while 0 <= dir < n:
            summ  += mat[dir][dir]
            dir += 1

        left = n - 1
        down = 0
        while 0 <= left < n and 0 <= left < n:
            summ += mat[down][left]
            left -= 1
            down += 1
        if n % 2 == 1:
            summ -= mat[(n-1)//2][(n-1)//2]
        return summ
        
        