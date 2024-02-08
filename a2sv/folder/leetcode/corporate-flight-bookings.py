class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n)
        for i, j , k in bookings:
            res[i - 1] += k
            if j  < n:
                res[j] -= k

        summ = 0
        for j in range(n):
            summ += res[j]
            res[j] = summ
        return res

        