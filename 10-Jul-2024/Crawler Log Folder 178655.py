# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for ch in logs:
            if stack and ch =="../":
                stack -= 1
            elif ch not in ["../", "./"]:
                stack += 1
        return stack
        