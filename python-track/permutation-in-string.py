class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])
        for i in range(len(s2) - len(s1) + 1):
            flag = True
            for l in s1:
                if count_s1[l] != count_s2.get(l,0):
                    flag = False
                    break
            if flag:
                return True
            if i + len(s1) < len(s2):
                count_s2[s2[i]] -= 1
                count_s2[s2[i + len(s1)]] = 1 + count_s2.get(s2[i + len(s1)],0)
        return False
        
        