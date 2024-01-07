class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count_0 = 0
        result = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count_0 += 1
            while count_0 > 1:
                if nums[i] == 0:
                    count_0 -= 1
                i += 1
            result = max(result, j - i)
        return result
        