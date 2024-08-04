# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:return True
        if n <= 1:return False
        return Solution.isPowerOfTwo(self,n/2)
        






