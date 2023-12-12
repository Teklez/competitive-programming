class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash = set()
        n = str(n)
        while n != '1':
            if n in hash:
                return False
            hash.add(n)
            n = str(sum([int(digit)**2 for digit in n]))
        return True
        



        