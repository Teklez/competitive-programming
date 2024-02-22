class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        catch = self.getRow(rowIndex - 1)
        res = [catch[i] + catch[i+1] for i in range(len(catch) - 1)]
        return [1] + res + [1]
        