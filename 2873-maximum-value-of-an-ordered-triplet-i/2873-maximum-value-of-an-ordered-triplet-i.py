class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Input: An array of integers 'nums'.
        # Output: The maximum triplet value.

        # Algorithm: Brute Force
        # Time Complexity: O(n^3)

        # res = 0
        # N = len(nums)

        # # Iterate through all possible 'j' indices.
        # for j in range(1, N - 1):
        #     # Find the maximum value to the left of 'j'.
        #     max_left = 0
        #     for i in range(j):
        #         max_left = max(max_left, nums[i])

        #     # Find the maximum value to the right of 'j'.
        #     max_right = 0
        #     for k in range(j + 1, N):
        #         max_right = max(max_right, nums[k])

        #     # Calculate the triplet value and update 'res'.
        #     value = (max_left - nums[j]) * max_right
        #     res = max(res, value)

        # # Return the final result.
        # return res if res > 0 else 0


        # Algorithm: Greedy (O(n^2) - less efficient)
        # Time Complexity: O(n^2)

        # res = 0
        # N = len(nums)
        # left = nums[0]

        # for j in range(1, N):
        #     if nums[j] > left:
        #         left = nums[j]
        #     for k in range(j + 1, N):
        #         res = max(res, (left - nums[j]) * nums[k])
        # return res


        # Algorithm: Pre-calculation (O(n) with O(n) space)
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # res = 0
        # N = len(nums)

        # # Pre-calculate 'left'.
        # left = [0] * N
        # left[0] = nums[0]
        # for i in range(1, N):
        #     left[i] = max(left[i - 1], nums[i])

        # # Pre-calculate 'right'.
        # right = [0] * N
        # right[N - 1] = nums[N - 1]
        # for i in range(N - 2, -1, -1):
        #     right[i] = max(right[i + 1], nums[i])

        # # Calculate max triplet value.
        # for j in range(1, N - 1):
        #     res = max(res, (left[j - 1] - nums[j]) * right[j + 1])
        # return res if res > 0 else 0


        # Algorithm: Optimized Single Pass Greedy (O(n) with O(1) space)
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # n = len(nums)
        
        # # Keep track of max (nums[i]) and max (nums[i] - nums[j]) so far.
        # max_i = 0
        # max_diff = 0
        # result = 0
        
        # for k in range(n):
        #     # Calculate max triplet value using previous max difference.
        #     # This represents max(nums[i] - nums[j]) * nums[k].
        #     result = max(result, max_diff * nums[k])
            
        #     # Update max difference seen so far (nums[i] - nums[k]).
        #     # This will be used in the next iteration.
        #     max_diff = max(max_i - nums[k], max_diff)
            
        #     # Update max value seen so far.
        #     max_i = max(max_i, nums[k])
            
        # return result

        # Algorithm: Optimized Single Pass Greedy (O(n) with O(1) space)
        left, diff, res = 0, 0, 0

        for i in nums:
            res = max(res, diff * i)
            diff = max(diff, left - i)
            left = max(left, i)
        return res