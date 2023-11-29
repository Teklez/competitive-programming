class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        reversed = 0
        while x > 0:
            reversed = reversed * 10 + x % 10
            x = x // 10
        return temp == reversed
    

        
        