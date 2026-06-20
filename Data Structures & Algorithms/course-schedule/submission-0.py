class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        UNVISITED = 0
        VISITED = 1
        VISITING = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            # Visited means at that node we have visited and not seen cycle
            if states[node] == VISITED:
                return True
            # Visiting means we've returned to the same node and there is a cycle
            elif states[node] == VISITING:
                return False
            
            states[node] = VISITING

            for neighbour in graph[node]:
                # If there is a cycle in neighbouring nodes, then Gaan
                if not dfs(neighbour):
                    return False
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        