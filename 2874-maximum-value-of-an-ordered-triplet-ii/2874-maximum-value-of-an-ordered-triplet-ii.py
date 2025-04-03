class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, diff, left = 0, 0, 0

        for i in nums:
            res = max(res, diff * i)
            diff = max(diff, left - i)
            left = max(left, i)
        return res
