class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1] ]< nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        print(res)
        for i in range(len(nums)):
            if i == stack[-1]:
                return res
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
        return res