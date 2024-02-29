class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        valid = []
        comb = []
        def combine(summ,i):
            if len(comb) > k:
                return
            if summ == n and len(comb) == k:
                valid.append(comb[:])
                return
            if i > 9:
                return
            
            comb.append(i)
            summ += i
            combine(summ, i + 1)
            summ -= i
            comb.pop()
            combine(summ,i + 1)

        combine(0,1)
        return valid


            

        