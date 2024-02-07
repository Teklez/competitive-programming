class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        runSum = [0]*len(nums)
        for i in range(len(nums)):
            summ += nums[i]
            runSum[i] = summ
        return runSum