class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        # pre = [0]*(points[-1][1] - points[0][0] + 1)
        n = len(points)

        # for i, j in points:
        #     pre[i - 1] += 1
        #     if j < len(pre):
        #         pre[j] -= 1
        # summ = 0
        # for i in range(len(pre)):
        #     summ += pre[i]
        #     pre[i] = summ
        # pre.sort(reverse=True)

        # res = 0
        # tot = 0
        # for  i in range(len(pre)):
        #     if tot == n:
        #         return res
        #     tot += pre[i]
        #     res += 1

        for i in range(len(points) - 1):
            if points[i][1] >= points[i + 1][0]:
                if points[i][1] > points[i + 1][1]:
                    points[i+1][1] = points[i + 1][1]
                else:
                    points[i+1][1] = points[i][1]
                n -= 1
        print(n)
        return n


