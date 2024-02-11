class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        preSum = {0:-1}
        minm = len(nums)
        runSum = 0
        tot = sum(nums)
        remainder = tot % p
        if p > tot:
            return -1
        if remainder == 0:
            return 0
        for i in range(len(nums)):
            runSum = (runSum + nums[i])%p
            if  (runSum - remainder)%p in preSum:
                minm = min(minm, i - preSum[(runSum - remainder)%p])
            preSum[runSum] = i
        return -1 if minm == len(nums) else minm

            