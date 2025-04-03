class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Algorithm: Greedy

        # Variables
        res, diff, left = 0, 0, 0

        # For loop
        for k in nums:
            res = max(res, diff * k)
            diff = max(diff, left - k)
            left = max(left, k)
        return res


        