class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # # Dynamic Programming

        # # Handle base cases
        # if n <= 2:
        #     return n
        
        # # Initialize dynamic programming
        # dp = [0] * (n + 1)
        # # One way to tile a 2x1 board
        # dp[1] = 1 
        # # Two ways to tile a 2x2 board
        # dp[2] = 2
        # # Five ways to tile a 2x3 board
        # dp[3] = 5

        # # Fill the dp array for subsequent board lengths
        # for i in range(4, n + 1):
        #     dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        # return dp[n]

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 0:
            return 0

        dp = [1, 1, 2]

        for i in range(3, n + 1):
            value = (dp[i - 3] + 2 * dp[i - 1]) % MOD
            dp.append(value)
        return dp[-1]



