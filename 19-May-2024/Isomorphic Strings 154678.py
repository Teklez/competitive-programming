# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        store = {}
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]] = t[i]
            else:
                if store[s[i]] != t[i]:
                    return False
        hash = {}
        for i in range(len(s)):
            if t[i] not in hash:
                hash[t[i]] = s[i]
            else:
                if hash[t[i]] != s[i]:
                    return False
        return True

        