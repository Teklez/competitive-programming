class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tot_distinct = len(set(nums))
        i, count = 0, 0
        for j in range(len(nums)):
            while len(set(nums[i:j+1])) == tot_distinct:
                count += len(nums) - j
                i += 1
        return count

        