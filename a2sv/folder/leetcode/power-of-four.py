class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:return True
        if n <= 1:return False
        return Solution.isPowerOfFour(self,n/4)
        