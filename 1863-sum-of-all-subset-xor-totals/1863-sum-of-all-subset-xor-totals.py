class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Input: an array nums
        # Output: the sum of all XOR totals for every subset of nums

        # Algorithm: Depth-First Search. Recursion
        def dfs(i, res):
            # If we've processed all elements, return the XOR total
            if i == len(nums):
                return res
            # Recursively calculate the sum by including or excluding the current element
            return dfs(i + 1, res ^ nums[i]) + dfs(i + 1, res)

        # Start with i 0 and an initial XOR total of 0
        return dfs(0, 0)
