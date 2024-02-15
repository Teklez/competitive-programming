class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res = (0,-1)
        need = len(set(t))
        have = 0
        countT = Counter(t)
        countS = defaultdict(int)
        minm = len(s) + 1
        i = 0
        for j in range(len(s)):
            countS[s[j]] += 1
            if countS[s[j]] == countT[s[j]]:
                have += 1
            while have == need:
                if j - i + 1 < minm:
                    res = [i, j]
                    minm = j - i + 1
                if countT[s[i]] == countS[s[i]]:
                    have -= 1
                countS[s[i]] -= 1
                i += 1
        return s[res[0]:res[1] + 1]
            



        
        