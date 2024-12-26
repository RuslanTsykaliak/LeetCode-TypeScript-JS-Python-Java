class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        
        for num in nums:
            next_dp = defaultdict(int)
            for current_sum, ways in dp.items():
                next_dp[current_sum + num] += ways
                next_dp[current_sum - num] += ways
            dp = next_dp

        return dp[target]