class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res, cor = [], [0,0]
        m, n = len(mat), len(mat[0])

        for i in range(1, n + m):
            dirc = [(-1)**i, -1*(-1)**i]
            while 0 <= cor[0] < m and 0 <= cor[1] < n:
                res.append(mat[cor[0]][cor[1]])
                cor[0] += dirc[0]
                cor[1] += dirc[1]

            cor[0] -= dirc[0]
            cor[1] -= dirc[1]

            if dirc[0] > 0:
                if cor[0] + 1 < m:
                    cor[0] += 1
                else:
                    cor[1] += 1
            elif dirc[1] > 0:
                if cor[1] + 1 < n:
                    cor[1] += 1
                else:
                    cor[0] += 1
        return res
            

            


        