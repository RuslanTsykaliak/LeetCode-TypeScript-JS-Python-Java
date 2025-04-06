class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if N <= 1:
            return nums

        nums.sort()

        dp = [1] * N
        parent = [-1] * N

        max_height = 1
        top_brick_i = 0

        for i in range(N):
            current_brick = nums[i]
            for j in range(i):
                previous_brick = nums[j]
                if current_brick % previous_brick == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            if dp[i] > max_height:
                max_height = dp[i]
                top_brick_i = i

        result = []
        current_i = top_brick_i
        while current_i != -1:
            result.append(nums[current_i])
            current_i = parent[current_i]

        return result[::-1]
