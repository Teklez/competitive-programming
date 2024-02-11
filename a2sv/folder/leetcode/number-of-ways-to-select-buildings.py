class Solution:
    def numberOfWays(self, s: str) -> int:
        building0 = 0
        building1 = 0
        tot0 = s.count("0")
        tot1 = s.count("1")
        validCount = 0
        for i in range(len(s)):
            validCount += (tot0 - building0)*(building0) if s[i] == "1" else (tot1 - building1)*(building1)
            if s[i] == "0":
                building0 += 1 
            else:
                building1 += 1
        return validCount


        