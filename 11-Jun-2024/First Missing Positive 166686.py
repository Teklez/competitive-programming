# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0

        while i < len(nums):
            current = nums[i] - 1

            if 0 < nums[i] < len(nums) and current != i and nums[i] != nums[current]:
                nums[current], nums[i] = nums[i], nums[current]
            else:
                i += 1

        for d in range(len(nums)):
            if nums[d] - 1 != d:
                return d + 1

        return len(nums) + 1







