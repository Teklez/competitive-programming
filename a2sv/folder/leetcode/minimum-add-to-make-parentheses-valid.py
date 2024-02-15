class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in range(len(s)):
            if not stack and s[i] == ")":
                count += 1
            elif stack and s[i] == ")":
                stack.pop()
            else:
                stack.append("(")
        while stack:
            stack.pop()
            count += 1
        return count
            

        