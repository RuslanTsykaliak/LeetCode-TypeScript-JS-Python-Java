class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Algorithm: Prefix Sum + Sliding Range
        lowest = highest = current = 0

        for diff in differences:
            current += diff
            if current < lowest:
                lowest = current
            if current > highest:
                highest = current
        
        differences_range = highest - lowest
        given_range = upper - lower
        res = (given_range - differences_range + 1)

        return max(0, res)
        