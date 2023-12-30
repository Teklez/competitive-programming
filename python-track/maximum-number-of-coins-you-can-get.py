class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        max_coin = 0
        i = len(piles) - 2
        for j in range(len(piles)//3):
            max_coin += piles[i]
            i -= 2
        return max_coin