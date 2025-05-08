class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        """
        Find the earliest time you can reach (n-1, m-1) from (0,0),
        given each room (i,j) unlocks at moveTime[i][j], and moves alternate
        between taking 1s and 2s.
        """
        n, m = len(moveTime), len(moveTime[0])
        # Four cardinal directions
        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

        # Min-heap of (current_time, x, y, next_step_cost)
        heap = [(0, 0, 0, 1)]
        # Mark start as visited
        moveTime[0][0] = -1

        while heap:
            time, x, y, step_cost = heapq.heappop(heap)

            # Explore neighbors
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if moveTime[nx][ny] < 0:
                    # already visited
                    continue

                # Can only enter room after it “unlocks”
                entry_time = max(time, moveTime[nx][ny]) + step_cost

                # If we’ve reached the goal, return immediately
                if nx == n-1 and ny == m-1:
                    return entry_time

                # Schedule this neighbor, mark visited
                heapq.heappush(heap, (entry_time, nx, ny, 3 - step_cost))
                moveTime[nx][ny] = -1

        # Problem guarantees there is always a path, so we never fall out here
