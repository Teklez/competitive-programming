# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = [[] for i in range(n)]
        incoming = {c:0 for c in range(n)}
        res = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            incoming[v] += 1
      
        queue = deque()
        for node in incoming:
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            cur = queue.popleft()
            for neighbour in graph[cur]:
                res[neighbour].add(cur)
                res[neighbour].update(res[cur])
                incoming[neighbour] -= 1
                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        res = [sorted((list(a))) for a in res]
        return res
        



