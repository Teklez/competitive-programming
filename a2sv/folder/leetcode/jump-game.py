class Solution:
    def canJump(self, nums: List[int]) -> bool:
        G = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if  nums[i] + i >= G:
                G = i
                print(i)
        return True if G == 0 else False


