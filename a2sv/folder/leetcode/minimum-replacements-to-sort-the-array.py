class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        min_op = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                divis = (nums[i] + nums[i + 1] - 1)//nums[i + 1]
                min_op += divis - 1
                nums[i] = nums[i]//divis
        return min_op

        