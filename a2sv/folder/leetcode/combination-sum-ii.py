class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()
        subset = []
        def combination(summ,i):
            if summ == target:
                if subset not in subsets:
                    subsets.append(subset[:])
                return
            if summ > target:
                return 

            if  i >= len(candidates):
                return

            subset.append(candidates[i])
            summ += candidates[i]
            combination(summ, i + 1)
            summ -= candidates[i]
            subset.pop()
            while i + 1 < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            combination(summ, i + 1)
        combination(0,0)
        return subsets
        