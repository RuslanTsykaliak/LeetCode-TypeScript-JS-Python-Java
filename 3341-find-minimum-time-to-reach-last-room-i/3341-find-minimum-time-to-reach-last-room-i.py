class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        n, m = len(moveTime), len(moveTime[0])
        dist = [[10**18]*m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (time, i, j)
        while pq:
            t, i, j = heapq.heappop(pq)
            if t > dist[i][j]: continue
            if (i, j) == (n-1, m-1):
                return t
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    depart = max(t, moveTime[ni][nj])
                    arrive = depart + 1
                    if arrive < dist[ni][nj]:
                        dist[ni][nj] = arrive
                        heapq.heappush(pq, (arrive, ni, nj))
        return -1