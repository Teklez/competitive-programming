# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        b = 0
        w = len(s) - 1
        count = 0
        while b < w:
            if s[w] == "0" and s[b] == "1":
                count += w - b
                w -= 1
                b += 1
            elif s[w] == "1":
                w -= 1
            else:
                b += 1
        return count













