class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exist = {}
        l = len(nums)
        for i in range(l):
            exist[nums[i]] = i
        
        for j in range(l + 1):
            if j not in exist:
                return j
