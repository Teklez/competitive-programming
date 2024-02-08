class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n + 1)
        for i, j , k in bookings:
            res[i] += k
            if j  < n:
                res[j + 1] -= k

        summ = 0
        for j in range(n + 1):
            summ += res[j]
            res[j] = summ
        return res[1:]

        