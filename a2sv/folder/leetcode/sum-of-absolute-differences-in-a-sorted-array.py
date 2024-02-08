class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        preSum = [0]*len(nums)
        postSum = [0]*len(nums)
        sumPre = 0
        sumPost = 0
        for i in range(len(nums)):
            preSum[i] = sumPre
            postSum[len(nums) - i -1] = sumPost
            sumPre += nums[i]
            sumPost += nums[len(nums) - i - 1]
        
        res = []
        for i in range(len(nums)):
            absolute = nums[i]*(i) - preSum[i] + postSum[i] - nums[i]*(len(nums) - i - 1)
            res.append(absolute)
        return res