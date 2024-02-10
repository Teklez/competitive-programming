class Solution:
    def bestClosingTime(self, customer: str) -> int:
        preSum = [0]*len(customer)
        postSum = [0]*len(customer)

        summN = 0
        summY = 0

        for i in range(len(customer)):
            if customer[len(customer) - i -1] == "Y":
                summY += 1
            postSum[len(customer) - i -1] = summY
            preSum[i] = summN
            if customer[i] == "N":
                summN += 1
        preSum.append(summN)
        postSum.append(0)

        minm = preSum[0] + postSum[0]
        res = 0
        for i in range(1,len(customer) + 1):
            if preSum[i] + postSum[i] < minm:
                minm = preSum[i] + postSum[i]
                res = i
        return res

            



