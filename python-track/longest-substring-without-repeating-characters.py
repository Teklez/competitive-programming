class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest_length = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in seen:
                seen[s[j]] = j
                if longest_length < len(seen):
                    longest_length = len(seen)
                j += 1
            else:
                del seen[s[i]]
                i += 1
        return longest_length
        