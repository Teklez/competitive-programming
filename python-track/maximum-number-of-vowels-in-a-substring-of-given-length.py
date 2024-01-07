class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a':1, "e":2, "i":3, "o":4, "u":5}
        i = 0
        maxx = 0
        vcount = 0
        for j in range(len(s)):
            if s[j] in vowels:
                vcount += 1
            if j - i + 1== k:
                maxx = max(vcount, maxx)
                if s[i] in vowels:
                    vcount -= 1
                i += 1
        return maxx
        