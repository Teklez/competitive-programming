class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost = 0
        for a, b in costs:
            totalCost += a
        refund = [b - a for a, b in costs]
        refund.sort()
        minCost = totalCost + sum(refund[:len(costs)//2])
        return minCost
