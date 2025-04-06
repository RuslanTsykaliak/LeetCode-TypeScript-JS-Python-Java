class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Input: a set of distinct positive integers nums
        # Output: retunr the largest subset answer
        # Constrains answer[i] % answer[j] == 0

        # Algorithm: Dynamic Programming
        # nums.sort()  # Sorting to make divisibility checks easier
        # dp = [[num] for num in nums]  # Initialize subsets with single elements
        # max_subset = []

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
        #             dp[i] = dp[j] + [nums[i]]  # Expand subset

        #     if len(dp[i]) > len(max_subset):  # Track the longest subset
        #         max_subset = dp[i]

        # return max_subset

        # Algorithm: ??? DP Tubulation
        # nums.sort()
        # dp = [[n] for n in nums] # dp[i] = longest start at i
        # res = []
        # for i in reversed(range(len(nums))):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] % nums[i] == 0:
        #             tmp = [nums[i]] + dp[j]
        #             dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
        #     res = dp[i] if len(dp[i]) > len(res) else res
        # return res

        # cache = {}
        # def dfs(i):
        #     if i == len(nums): return []
        #     if i in cache: return chache[i]

        #     res = [nums[i]]
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] % nums[i] == 0:
        #             tmp = [nums[i]] + dfs(j)
        #             if len(tmp) > len(res):
        #                 res = tmp
        #     cache[i] = res
        #     return res
        
        # res = []
        # for i in range(len(nums)):
        #     tmp = dfs()
        #     if len(tmp) > len(res):
        #         res = tmp
        # return res

        # Algorithms: ???
        # Runtime Beats 99.91
        # d = {}
        # nums = sorted(nums)
        # d[1] = [[nums[0]]]
        # max_level = 1
        # for num in nums[1:]:
        #     inserted = False
        #     for level in range(max_level, 0, -1):
        #         for l in d[level]:
        #             if num % l[-1] == 0:
        #                 if level + 1 > max_level:
        #                     d[level + 1] = [l + [num]]
        #                     max_level += 1
        #                 else:
        #                     d[level + 1] += [l + [num]]
        #                 inserted = True
        #                 break
        #         if inserted:
        #             break
        #         if level == 1 and l == d[level][-1]:
        #             d[1] += [[num]]
        # return d[max_level][0]

        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))


        
