class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # We cannot use Brute Force solution as 10^9 + 7 to big for checking every path
        # Dijkstra's Algorithm

        # Grapths are usually represented as adjacency lists
        # Simple and efficient way to store all neighbors and edge weights
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))

        MOD = 10**9 + 7
        # Greedy: Min-Heap is used to always process the node with the smallest cost/weight first
        min_heap = [(0, 0)]  # (cost, node)
        min_cost = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)

            for nei_cost, nei in adj[node]:
                # Relaxation Check if the current path gives a better (smaller) cost
                # update distance and push to heap
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (cost + nei_cost, nei))
                elif cost + nei_cost == min_cost[nei]:
                    # Modulo: Avoide larger number overflows
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD
        return path_count[n - 1]
