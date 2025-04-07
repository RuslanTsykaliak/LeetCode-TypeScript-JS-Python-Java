class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Input: an integer array
        # Output: True | False
        # Rules: the array should be slit into two equal parts.
        # For example, nums = [1, 3, 4] return True
        # because [1, 3] == [4]

        # Algorithm: Dynamic Programming
        coins = sum(nums)
        if coins & 1:
            return False

        equal_share = coins // 2
        dp = [False] * (equal_share + 1)
        dp[0] = True

        for coin in nums:
            # Travers backward to avoid reusing the same num
            for s in range(equal_share, coin - 1, -1):
                # Either we already could reach s, or we can reach s - num and add num
                dp[s] = dp[s] or dp[s - coin]

        return dp[equal_share]
