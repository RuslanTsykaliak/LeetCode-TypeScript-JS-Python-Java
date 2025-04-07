class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        coins = sum(nums)
        if coins & 1:
            return False
        
        equal_share = coins // 2

        dp = [False] * (equal_share + 1)
        dp[0] = True

        for coin in nums:
            for s in range(equal_share, coin - 1, -1):
                dp[s] = dp[s] or dp[s - coin]
        return dp[equal_share]
        
        