class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0 
        while target > 1:
            res += 1 if target % 2 == 1 else 0
            target = target if target % 2 == 0 else target - 1
            if maxDoubles > 0:
                target  //= 2
                res += 1
                maxDoubles -= 1
            else:
                res += (target - 1)
                target = 1
        return res
            


        