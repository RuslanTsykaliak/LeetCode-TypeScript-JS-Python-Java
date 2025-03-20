# Union Find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Connects x and y
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]


class Solution:
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        # Build Components
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        # Get cost of each component
        component_cost = {}  # root -> cost
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        # Queries
        res = []
        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])
        return res
