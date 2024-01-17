class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            nums[i] = summ
        return nums
            