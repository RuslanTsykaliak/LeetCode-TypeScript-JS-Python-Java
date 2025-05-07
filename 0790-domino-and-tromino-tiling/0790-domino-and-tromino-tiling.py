class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        # Initialize with the three base cases
        a, b, c = 1, 1, 2  # a=dp[0], b=dp[1], c=dp[2]
        
        for i in range(3, n+1):
            # Calculate next value and rotate variables
            current = (a + 2 * c) % MOD
            a, b, c = b, c, current
        
        return c