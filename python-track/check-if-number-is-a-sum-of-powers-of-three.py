class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = int(math.log(n, 3))
        tot = 0
        while power >= 0:
            if tot + 3**power < n:
                tot += 3**power
            elif tot + 3**power == n: return True
            power -= 1
        return False


        