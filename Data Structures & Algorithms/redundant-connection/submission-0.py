class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        # Initially every node is its own parent
        parent = [i for i in range(n+1)]

        def find(node):
            if parent[node] != node:
                # Path compression
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            parent[rootB] = rootA
            return True

        for u, v in edges:
            # If union fails,
            # u and v were already connected
            if not union(u, v):
                return [u, v]