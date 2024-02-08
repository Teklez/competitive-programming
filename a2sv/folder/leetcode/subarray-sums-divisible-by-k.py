class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        summ = 0
        res = 0
        for i in range(len(nums)):
            summ += nums[i]
            res += count.get(summ % k , 0)
            count[summ % k] = count.get(summ % k, 0) + 1
        return res

        