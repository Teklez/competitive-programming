class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        tot = 0
        for i in range(len(costs)):
            if tot + costs[i] > coins:
                return i
            tot += costs[i]
        return i + 1

        