class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(1,len(nums)):
            while nums[i] != 0 and i < j:
                i += 1
            if nums[j] != 0 and i < j:
                nums[j], nums[i] = nums[i], nums[j]
        