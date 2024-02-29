class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()
        subset = []
        def combination(summ,i):
            if summ > target:
                return 
            if  i >= len(candidates):
                return
            if summ == target:
                subsets.append(subset[:])
                return
            subset.append(candidates[i])
            summ += candidates[i]
            combination(summ, i)
            summ -= candidates[i]
            subset.pop()
            combination(summ, i + 1)
        combination(0,0)
        return subsets