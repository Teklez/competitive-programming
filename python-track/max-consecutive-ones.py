class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, i - last - 1)
                last = i
        res = max(res, i - last)
        return res

 
            