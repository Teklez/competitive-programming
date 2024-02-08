class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        preSum = [0]*trips[-1][-1]

        for i, j, k in trips:
            preSum[j] += i
            if k < trips[-1][-1]:
                preSum[k] -= i
        print('pre', preSum)
        summ = 0
        for j in range(trips[-1][-1]):
            summ += preSum[j]
            preSum[j] = summ
            if preSum[j] > capacity:
                return False
        return True
        