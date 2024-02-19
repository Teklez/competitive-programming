class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for ch in path:
            if stack and ch == "..":
                stack.pop()
            elif ch not in [".", "", ".."]:
                stack.append(ch)
        return "/" + "/".join(stack)