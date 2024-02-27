class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def combination(subset,i):
            if subset not in subsets:
                subsets.append(subset[:])
            if i >= len(nums):
                return
            subset.append(nums[i])
            combination(subset, i + 1 )
            subset.pop()
            combination(subset, i + 1)
        combination([], 0)
        return subsets




        
        