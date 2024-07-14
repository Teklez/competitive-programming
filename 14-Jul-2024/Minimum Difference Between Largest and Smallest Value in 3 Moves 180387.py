# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        return 0 if len(nums)<=4 else nums.sort() or min(nums[len(nums)-4+i]-nums[i] for i in range(4))
        