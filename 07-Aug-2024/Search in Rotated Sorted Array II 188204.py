# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = len(nums) - 1
        for j in range(len(nums)):
            if nums[j] == target:
                return True
            if j + 1 < len(nums) and nums[j] > nums[j + 1]:
                pivot = j

        i = (pivot + 1) % len(nums)
        while i != pivot:
            if nums[i] == target:
                return True
            i = (i + 1) % len(nums)
        return False
        