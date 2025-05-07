class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        # dist[r][c] stores the minimum time to ARRIVE at room (r,c)
        dist = [[float('inf')] * m for _ in range(n)]

        # We start at (0,0) at t=0. So, arrival time at (0,0) is 0.
        dist[0][0] = 0
        
        # Priority queue stores (arrival_time_at_current_cell, r, c)
        pq = [(0, 0, 0)] 

        # Movement directions: right, left, down, up
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        while pq:
            current_arrival_time, r, c = heapq.heappop(pq)

            # If we found a shorter path to (r,c) already, skip
            if current_arrival_time > dist[r][c]:
                continue

            # If we reached the destination cell (n-1, m-1)
            if r == n - 1 and c == m - 1:
                return current_arrival_time

            # Explore neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check if the neighbor is within grid boundaries
                if 0 <= nr < n and 0 <= nc < m:
                    # current_arrival_time is the time we arrived at cell (r,c).
                    # We want to move to neighbor (nr,nc).
                    # The earliest we can START this move from (r,c) to (nr,nc) is
                    # determined by both when we are ready at (r,c) (i.e., current_arrival_time)
                    # and the constraint moveTime[nr][nc] for entering (nr,nc).
                    departure_from_rc_time = max(current_arrival_time, moveTime[nr][nc])
                    
                    # The move itself takes 1 second.
                    new_arrival_time_at_neighbor = departure_from_rc_time + 1
                    
                    # If this path offers a
                    # shorter time to arrive at (nr,nc)
                    if new_arrival_time_at_neighbor < dist[nr][nc]:
                        dist[nr][nc] = new_arrival_time_at_neighbor
                        heapq.heappush(pq, (new_arrival_time_at_neighbor, nr, nc))
        
        return -1 # Should ideally not be reached if a path always exists as per typical problem constraints.
                  # Or if problem guarantees reachability. Given the problem setup, a path is expected.