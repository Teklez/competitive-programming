class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        counts = Counter(s)
        res = 0
        rem = 0
        for char, count in counts.items():
            res += (count//2)*2
            rem = max(count%2, rem)
        if rem:
            res += 1
        return res


        