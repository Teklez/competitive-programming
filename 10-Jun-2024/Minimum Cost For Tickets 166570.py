# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dp(i, covered_until):
            if i >= len(days):
                return 0
            
            if (i, covered_until) not in memo:

                if days[i] > covered_until:
                    one_day_ticket = costs[0] + dp(i + 1, days[i])
                    seven_day_ticket = costs[1] + dp(i + 1, days[i] + 6)
                    therteen_day_ticket = costs[2] + dp(i + 1, days[i] + 29)
                    memo[(i, covered_until)] = min(one_day_ticket, seven_day_ticket, therteen_day_ticket)
                else:
                    memo[(i, covered_until)] = dp(i + 1, covered_until)

            return memo[(i, covered_until)]
        return dp(0, 0)



        






