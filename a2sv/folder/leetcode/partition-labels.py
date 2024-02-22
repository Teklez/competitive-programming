class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        res = []
        mx = 0
        i = 0
        for j in range(len(s)):
            if last[s[j]] == j and mx <= j:
                res.append(j - i + 1)
                if j < len(s) - 1:
                    mx = last[s[j + 1]]
                i = j + 1
            mx = max(mx, last[s[j]])
        return res
            


        