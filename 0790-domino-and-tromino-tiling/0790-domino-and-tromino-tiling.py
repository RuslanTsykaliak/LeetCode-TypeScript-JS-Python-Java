class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        # Handle small n directly
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        dp = [1, 1, 2]  # dp[0], dp[1], dp[2]
        for i in range(3, n + 1):
            dp.append((2 * dp[i-1] + dp[i-3]) % MOD)
        return dp[n]