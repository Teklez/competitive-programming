class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult1 = [0]*len(nums)
        mult1 = mult2 = 1

        prefix_mult2 = [0]*len(nums)

        for i in range(len(nums)):
            mult1 *= nums[i]
            prefix_mult1[i] = mult1

        for j in range(len(nums) - 1,-1,-1):
            mult2 *= nums[j]
            prefix_mult2[j] = mult2
        for k in range(len(nums)):
            if k == 0:
                nums[k] = prefix_mult2[1]
            
            elif k == len(nums) - 1:
                nums[k] = prefix_mult1[k - 1]
            
            else:
                nums[k] = prefix_mult1[k - 1] * prefix_mult2[k + 1]

        return nums
        