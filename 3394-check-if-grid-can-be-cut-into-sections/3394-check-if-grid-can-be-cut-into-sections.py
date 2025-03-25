class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Greedy Interval Selection
        # Extract x-coordinate intervals (left, right edges)
        x = [(r[0], r[2]) for r in rectangles]
        # Extract y-coordinate intervals (bottom, top edges)
        y = [(r[1], r[3]) for r in rectangles]

        # Sort intervals for efficient processing (greedy interval selection)
        x.sort()
        y.sort()

        def count_non_overlapping(intervals):
            # Counts the number of non-overlapping intervals
            count = 0
            # Tracks the end of the last selected interval
            prev_end = -1
            # Iterate through the sorted intervals
            for start, end in intervals:
                # If the current interval doesn't overlap with the previous one, select it
                if prev_end <= start:
                    count += 1
                # Update the end of the last selected interval
                prev_end = max(prev_end, end)
            return count

        # Return True if the maximum number of non-overlapping intervals in either x or y is >= 3
        return max(count_non_overlapping(x), count_non_overlapping(y)) >= 3
