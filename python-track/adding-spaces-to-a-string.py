class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        i = len(s) - 1
        while i >= 0:
            ans.append(s[i])
            if spaces and i == spaces[-1]:
                ans.append(' ')
                spaces.pop()
            i -= 1    
        return ''.join(ans[:: -1])
        