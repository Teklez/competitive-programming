class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        prefix = []
        for j in range(len(matrix)):
            prefix.append([0]*len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i !=0 and j != 0:
                    prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + matrix[i][j]
                elif i == 0:
                    prefix[i][j] = prefix[i][j - 1] + matrix[i][j]
                else:
                    prefix[i][j] = prefix[i - 1][j] + matrix[i][j]
                    

        
        self.prefix = prefix
        print(prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        if col1 != 0 and row1 != 0:
            res += self.prefix[row2][col2] - self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col2] + self.prefix[row1 - 1][col1 - 1]
        elif col1 != 0:
            res += self.prefix[row2][col2] - self.prefix[row2][col1 - 1]
        elif row1 != 0:
            res += self.prefix[row2][col2] - self.prefix[row1 - 1][col2]
        else:
            res += self.prefix[row2][col2]


        return res


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)