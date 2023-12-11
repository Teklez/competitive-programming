class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        num_s = {}
        for j in range(len(nums)):
            num_s[nums[j]] = j

        for i in range(len(operations)):
            index = num_s[operations[i][0]]
            nums[index] = operations[i][1]
            del num_s[operations[i][0]]
            num_s[operations[i][1]] = index

        return nums
            
