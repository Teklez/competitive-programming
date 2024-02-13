class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def maximum(dic):
            maxm = 0
            for key, value in dic.items():
                maxm = max(maxm, value)
            return maxm
        
        count = {}
        maxm = 0
        i = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            window = j - i + 1
            while window - maximum(count) > k:
                count[s[i]] -= 1
                i += 1
                window = j - i + 1
            maxm = max(maxm, j - i + 1)
        return maxm
