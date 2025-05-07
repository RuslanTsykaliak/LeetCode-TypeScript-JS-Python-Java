class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        if n == 1 and m == 1:
            return 0

        visited = set()
        visited.add((0, 0))

        h = [(0, 0, 0)]
        while h:
            t, x, y = heappop(h)
            if (x, y) == (n - 1, m - 1):
                return t
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                u, v = x + dx, y + dy
                if 0 <= u < n and 0 <= v < m and (u, v) not in visited:
                    heappush(h, (max(t, moveTime[u][v]) + 1, u, v))
                    visited.add((u, v))
        return -1