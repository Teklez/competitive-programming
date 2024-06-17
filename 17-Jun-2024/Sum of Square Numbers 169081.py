# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        devisor = int(math.sqrt(c))
        j = devisor
        while  i <= j :
            print(i, j)
            
            if i*i + j*j == c:
                return True
            elif i*i + j*j < c :
                i += 1
            else:
                j -= 1
        return False
        