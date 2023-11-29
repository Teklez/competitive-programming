class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        devisor = n
        while True:
            if n % devisor == 0 and n % 2 == 0:
                return n
            n += 1
