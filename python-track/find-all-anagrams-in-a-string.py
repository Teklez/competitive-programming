class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = Counter(p)
        countS = Counter(s[:len(p)])
        anagrams = []
        for i in range(len(s) - len(p) + 1):
            if countP == countS:
                anagrams.append(i)
                
            if i + len(p) < len(s):
                countS[s[i]] -= 1
                countS[s[i + len(p)]] = 1 + countS[s[i + len(p)]]
        return anagrams
        