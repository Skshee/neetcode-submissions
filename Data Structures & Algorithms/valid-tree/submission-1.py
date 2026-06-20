class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there is no cycle and all edges are connected, it's a tree
        graph = defaultdict(list)
        visited = set()

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node, parent):
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei in visited:
                    return False # CYCLE
                if not dfs(nei, node):
                    return False

            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n


            
        