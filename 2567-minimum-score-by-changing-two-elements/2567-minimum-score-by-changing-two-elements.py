class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        mn1 = mn2 = mn3 = inf
        mx1 = mx2 = mx3 = -inf

        for x in nums:
            if x < mn1:
                mn1, mn2, mn3 = x, mn1, mn2
            elif x < mn2:
                mn2, mn3 = x, mn2
            elif x < mn3:
                mn3 = x

            if x > mx1:
                mx1, mx2, mx3 = x, mx1, mx2
            elif x > mx2:
                mx2, mx3 = x, mx2
            elif x > mx3:
                mx3 = x

        return min(mx1 - mn3, mx2 - mn2, mx3 - mn1)
