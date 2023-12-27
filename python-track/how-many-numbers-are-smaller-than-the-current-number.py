class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = []
        for w in range(1,len(nums) + 1):
            i = 0
            count = 0
            for j in range(1,len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            counts.append(count)
            if w < len(nums):
                nums[0],nums[w] = nums[w],nums[0]
        return counts
        
        