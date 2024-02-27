class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def combination(subset,k):
            if len(subset) == k:
                subsets.append(subset[:])
            last = nums.index(subset[-1]) if subset else -1
            for cur in (nums[last + 1:]):
                subset.append(cur)
                combination(subset,k)
                subset.pop()
        for i in range(len(nums) + 1):
            combination([], i)
        return subsets


        