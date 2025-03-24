class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Input: 2D array 'meetings' where each element is [start_day, end_day].
        # Output: The number of working days that have no meetings.

        # Algorithm Pattern: Greedy with Interval Merging
        # The algorithm uses a greedy approach to iterate through the meetings,
        # merging overlapping intervals and calculating the total number of meeting days.

        # Sort the meetings by start day to process them in chronological order.
        meetings.sort()

        # 'prev_day' keeps track of the latest meeting end day processed.
        prev_day = 0

        # Iterate through the meetings.
        for start, end in meetings:
            # Adjust the 'start' day to avoid double-counting overlapping meeting days.
            start = max(start, prev_day + 1)

            # Calculate the length of the meeting interval.
            length = end - start + 1

            # Subtract the meeting days from the total working days.
            days -= max(length, 0)

            # Update 'prev_day' to the latest meeting end day.
            prev_day = max(prev_day, end)

        # Return the remaining working days.
        return days
