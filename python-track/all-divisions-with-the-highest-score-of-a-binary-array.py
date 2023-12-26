class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        summ = [0]*(len(nums) + 1)
        tot = 0
        for i in range(len(nums) - 1, -1, -1):
            tot += nums[i]
            summ[i] = tot

        count = 0
        maxm = float('-inf')
        res=[]

        for j in range(len(nums) + 1):
            current = count + summ[j]
            if current > maxm:
                maxm = current
                res = []
                res.append(j)
            elif current == maxm:
                res.append(j)
            if j < len(nums) and not nums[j]:
                count += 1
        return res



        