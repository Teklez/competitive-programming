class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_avg = 0
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            max_avg = max(pre_sum/(i + 1), max_avg)
        return math.ceil(max_avg)