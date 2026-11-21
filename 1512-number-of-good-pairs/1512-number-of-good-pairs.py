class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # Input: array of integers
        # Output: integer, condition nums[i] == nums[j] and i < j

        n = len(nums)
        good_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        
        return good_pairs
