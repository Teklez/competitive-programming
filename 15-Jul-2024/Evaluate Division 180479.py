# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create an adjescency list
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((values[i], equations[i][1]))
            graph[equations[i][1]].append((1/values[i], equations[i][0]))

        res = [-1]*len(queries)

        def dfs(node, source, destination, i):
            if node[1] in visited:
                return

            visited.add(node[1])

            if node[1] == destination:
                res[i] = node[0] * source[0]

                return

            for neighbour in graph[node[1]]:

                if neighbour[1] not in visited:
                    mult = node[0]*source[0]
                    dfs(neighbour, (mult, node[1]), destination, i)
    
    
        for i in range(len(queries)):
            visited = set()
            if queries[i][0]  in graph and queries[i][1] in graph:
                dfs((1, queries[i][0]), (1, queries[i][0]),queries[i][1], i)
        
        return res

                    

