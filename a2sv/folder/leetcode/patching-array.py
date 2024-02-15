class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        pre = 0
        for i in range(len(nums)):
            if n <= nums[i]:
                nums[i] = n
                break
        i += 1
        if i == len(nums):
            nums.append(n)
        for i in range(len(nums)):
            while pre + 1 < nums[i]:
                pre += pre + 1
                patches += 1
            if pre >= n:
                break
            pre += nums[i]
        print(nums)
        return patches
            

        


        