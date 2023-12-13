class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            p1 = points[i - 1][0]
            p2 = points[i - 1][1]
            p3 = points[i][0]
            p4 = points[i][1]
            time += max(abs(p3 - p1) , abs(p4 - p2))

        return time

