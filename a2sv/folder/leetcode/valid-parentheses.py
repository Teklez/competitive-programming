class Solution:
    def isValid(self, s: str) -> bool:
        openning = "([{"
        closing = ")]}"
        container = []
        for i in range(len(s)):
            if s[i] in openning:
                container.append(s[i])
            elif s[i] in closing:
                if len(container) == 0 or closing.find(s[i])  != openning.find(container.pop()):
                    return False
        return len(container) == 0