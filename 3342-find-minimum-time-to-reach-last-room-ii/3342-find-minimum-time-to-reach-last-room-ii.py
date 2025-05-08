from bisect import bisect_left


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # LOGIC: Djikstra
        # We keep a sorted queue ('options') to tell us which cell we can visit next based on the cells we have
        # already visited till now. The choice is the option which has the lowest possible time

        offsets = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]  # Offsets to identify the adjaccent cells
        n, m = len(moveTime), len(moveTime[0])  # Find Dimensions

        # Initial boundary conditions
        options = [
            [0, 0, 0, 1]
        ]  # First elem is time taken, next two are coordinates, next step (1s or 2s)
        moveTime[0][
            0
        ] = (
            -1
        )  # Since we have already added this element to the queue, we mark it as visited

        # In every iteration, pop the cell from the queue having the lowest time. Then look at its adjacent
        # cells to compute the time taken to visit them from the cell popped. Post this, create an entry for
        # each of these cells and add them to the queue (in a sorted fashion) and mark them as visited
        while True:
            t, x, y, dt = options.pop(0)  # Pop the cell with the smallest time
            for dx, dy in offsets:
                x_new, y_new = x + dx, y + dy  # Each adjacent and non-visited cell
                if 0 <= x_new < n and 0 <= y_new < m and moveTime[x_new][y_new] != -1:
                    t_new = (
                        max(t, moveTime[x_new][y_new]) + dt
                    )  # Calculate the time taken to reach this cell
                    if x_new == n - 1 and y_new == m - 1:
                        return t_new  # Answer returned when we reach end point for the first time

                    entry = [
                        t_new,
                        x_new,
                        y_new,
                        dt % 2 + 1,
                    ]  # Information for the adjacent cell
                    idx = bisect_left(options, entry)  # Inserting in the sorted queue
                    options.insert(idx, entry)

                    moveTime[x_new][y_new] = -1  # Mark adjacent cell as visited
