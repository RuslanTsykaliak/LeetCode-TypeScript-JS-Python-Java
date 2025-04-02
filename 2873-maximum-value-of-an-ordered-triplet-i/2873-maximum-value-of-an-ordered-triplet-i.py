class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Input: an array of integers nums
        # Output: an integer with the maximum value over all triplets of indices
        
        # Algorithm: Burute Force

        res = 0
        N = len(nums)

        # Iterate through all possible j indices
        for j in range(1, N - 1):
            # Find the maximum value to the left of j
            max_left = 0
            for i in range(j):
                max_left = max(max_left, nums[i])

            # Find the maximum value to the right of j
            max_right = 0
            for k in range(j + 1, N):
                max_right = max(max_right, nums[k])

            # Calculate the triplet value and update res
            value = (max_left - nums[j]) * max_right
            res = max(res, value)

        # Return the final result
        return res if res > 0 else 0
