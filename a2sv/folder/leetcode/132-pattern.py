class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minm = nums[0]
        for i in range(len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            if stack and stack[-1][-1] < nums[i]:
                return True
            stack.append((nums[i], minm))
            minm = min(minm, nums[i])
        return False