class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        visited = {}
        for path in paths:
            splitted = path.split()
            for i in range(1,len(splitted)):
                index = splitted[i].index("(")
                if splitted[i][index:] in visited:
                    visited[splitted[i][index:]].append("/".join([splitted[0],splitted[i][:index]]))
                else:
                    visited[splitted[i][index:]] = ["/".join([splitted[0],splitted[i][:index]])]
        
        return [val for val in visited.values() if len(val) > 1]