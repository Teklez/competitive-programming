class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        summ = 0
        res = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - goal in count:
                res += count[summ - goal]
            count[summ] = count.get(summ, 0) + 1
        return res