class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        if len(digits) == 0:
            return res
        def combine(temp,i):
            if len(temp) == len(digits) and temp not in res:
                res.append(temp)
                return
            for d in range(i, len(digits)):
                for c in maps[digits[i]]:
                    temp += c
                    combine(temp,i + 1)
                    temp = temp[:-1]
        combine("",0)
        return res

