class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # preSum = [0]*len(nums)
        # postSum = [0]*len(nums)
        # sumPre = 0
        # sumPost = 0
        # for i in range(len(nums)):
        #     preSum[i] = sumPre
        #     postSum[len(nums) - i -1] = sumPost
        #     sumPre += nums[i]
        #     sumPost += nums[len(nums) - i - 1]
        
        # res = []
        tot, preSum = sum(nums), 0
        for i in range(len(nums)):
            preSum += nums[i]
            nums[i] = nums[i]*(i + 1) - preSum + (tot - preSum) - nums[i]*(len(nums) - i - 1)
        return nums