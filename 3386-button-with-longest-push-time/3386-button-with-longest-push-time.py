class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        # 
        maxTime = events[0][1]
        res = events[0][0]

        for i in range(1, len(events)):
            pressTime = events[i][1] - events[i - 1][1]
            if pressTime > maxTime or (pressTime == maxTime and events[i][0] < res):
                maxTime = pressTime
                res = events[i][0]
        return res
