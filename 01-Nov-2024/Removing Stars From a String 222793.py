# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*" and stack:
                stack.pop()
            elif ch != "*":
                stack.append(ch)
        return "".join(stack)
        