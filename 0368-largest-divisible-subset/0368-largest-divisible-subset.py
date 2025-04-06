class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Input: a set of distinct positive integers nums
        # Output: retunr the largest subset answer
        # Constrains answer[i] % answer[j] == 0

        # Algorithm: Dynamic Programming
        nums.sort()  # Sorting to make divisibility checks easier
        N = len(nums)
        dp = [[num] for num in nums]  # Initialize subsets with single elements
        max_subset = []

        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]  # Expand subset

            if len(dp[i]) > len(max_subset):  # Track the longest subset
                max_subset = dp[i]

        return max_subset
