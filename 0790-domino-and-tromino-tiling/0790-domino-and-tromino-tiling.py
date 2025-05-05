class Solution:
    def numTilings(self, n: int) -> int:
        # Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        MOD = 10**9 + 7
        # Base cases
        if n == 1: return 1
        if n == 2: return 2
        if n == 0: return 0

        dp = [1, 1, 2]

        for i in range(3, n+1):
            value = (dp[i-3] + 2 * dp[i-1]) % MOD
            dp.append(value)
        
        return dp[-1]