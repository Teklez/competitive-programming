# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            incoming[u] += 1
            incoming[v] += 1
        
        queue = deque()
        for i in range(n):
            if incoming[i] <= 1:
                queue.append(i)
        
        while queue:
            if n <= 2:
                return queue
            for _ in range(len(queue)):
                cur = queue.popleft()
                n -= 1
                for neighbour in graph[cur]:
                    incoming[neighbour] -= 1
                    if incoming[neighbour] == 1:
                        queue.append(neighbour)

        return queue
                

