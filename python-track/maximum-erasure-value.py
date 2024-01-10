class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash = {}
        i = 0
        maxx = 0
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            hash[nums[j]] = hash.get(nums[j], 0) + 1
            while hash[nums[j]] > 1:
                hash[nums[i]] -= 1
                summ -= nums[i]
                i += 1
            maxx = max(maxx, summ)
        return maxx
        