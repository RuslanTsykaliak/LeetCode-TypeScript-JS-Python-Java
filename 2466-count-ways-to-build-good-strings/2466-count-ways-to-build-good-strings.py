class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1000000007

        def helper(curr):
            # before adding, check if length excedes high
            if curr > high:
                return 0

            ans = helper(curr + zero) + helper(curr + one)

            # if the string is good, add it to the count
            if low <= curr:
                ans += 1

            return ans % mod

        return helper(0)
