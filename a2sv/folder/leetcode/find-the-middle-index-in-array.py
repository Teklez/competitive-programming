class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = [0] * (len(nums))
        post = [0] *(len(nums))

        totPre = 0
        totPost = 0
        for i in range(len(nums)):
            pre[i] = totPre
            post[len(nums) - i - 1] = totPost
            totPre += nums[i]
            totPost += nums[len(nums) - i - 1]

        for j in range(len(nums)):
            if pre[j] == post[j]:
                return j
        return -1

            

        