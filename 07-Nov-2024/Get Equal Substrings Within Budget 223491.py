# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cur_max, max_len = 0, 0
        l = 0 
        for r in range(len(s)):
            cur_max += abs(ord(s[r]) - ord(t[r]))
            while l <= r and cur_max > maxCost:
                cost = abs(ord(s[l]) - ord(t[l]))
                cur_max -= cost
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len