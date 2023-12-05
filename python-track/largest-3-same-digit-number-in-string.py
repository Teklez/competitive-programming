class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        res = 0
        for j in range(2, len(num)):
            if len(set(num[i:j + 1])) == 1:
                if int(num[i:j + 1]) >= int(res):
                    res = num[i:j + 1]
            i += 1
        return "" if res == 0 else res
                


        