class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_left = values[0]

        for j in range(1, len(values)):
            max_score = max(max_score, max_left + values[j] - j)
            max_left = max(max_left, values[j] + j)

        return max_score
