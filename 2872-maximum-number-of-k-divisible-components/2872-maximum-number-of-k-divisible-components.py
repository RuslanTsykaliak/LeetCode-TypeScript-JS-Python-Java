class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        N = len(edges) + 1
        graph = {i: set([]) for i in range(N)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        self.res = 0
        values = [v % k for v in values]

        @cache
        def dfs(node, parent):
            val = values[node]
            for child in graph[node]:
                if child == parent:
                    continue
                val += dfs(child, node)
            val = val % k
            if val == 0:
                self.res += 1
            return val

        dfs(0, -1)
        return self.res
