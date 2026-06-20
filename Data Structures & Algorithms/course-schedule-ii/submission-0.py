class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1 - Build order as if a topological ordering might exist.
        # 2 - If a cycle is ever found:
        # abandon everything,
        # return [].
        # 3 - Otherwise:
        # return the completed ordering.

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        graph = defaultdict(list)
        order = []

        for x,y in prerequisites:
            graph[x].append(y)

        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED:
                return True
            elif states[node] == VISITING:
                return False

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            order.append(node)
            return True
        
        for i in range(numCourses):
            # If there is a cycle
            if not dfs(i):
                return []
        return order
