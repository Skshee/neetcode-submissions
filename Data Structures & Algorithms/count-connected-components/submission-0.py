class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()
        components = 0

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        print(graph)

        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                components += 1
                dfs(i)
        return components