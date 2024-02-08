class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        summ = 0
        maxm = 0
        for i in range(len(s) - 1):
            summ += int(s[i])
            maxm = max(i + 1 + ones - 2*summ, maxm)
        return maxm


        