class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        i = 1
        av = summ/k
        for j in range(k, len(nums)):
            summ = summ - nums[i-1] + nums[j]
            av = max(summ/k,av)
            i += 1
        return av

        