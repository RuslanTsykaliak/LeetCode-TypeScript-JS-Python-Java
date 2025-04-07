class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Input: an integer array
        # Output: True | False
        # Rules: the array should be slit into two equal parts.
        # For example, nums = [1, 3, 4] return True
        # because [1, 3] == [4]

        # Algorithm: Dynamic Programming
        coins = sum(nums)
        if coins % 2 != 0:
            return False

        n = len(nums)
        equal_share = coins // 2 
        dp = [[False] * (equal_share + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(equal_share + 1):
                if j < num:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
        return dp[n][equal_share]