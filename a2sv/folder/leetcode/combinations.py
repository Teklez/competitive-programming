class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(combine):
            nonlocal res
            if len(combine) == k:
                res.append(combine[:])
            last = combine[-1] if combine else 0
            for cur_last in range(last + 1, n + 1):
                combine.append(cur_last)
                backtrack(combine)
                combine.pop()
        backtrack([])
        return res

        

        