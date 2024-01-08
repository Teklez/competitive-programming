class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        summ = 0
        i = 0
        for j in range(len(nums)):
            summ += nums[j]
            while summ >= target:
                summ -= nums[i]
                min_len = min(min_len, j - i + 1)
                i += 1
        return min_len if min_len <= len(nums) else 0