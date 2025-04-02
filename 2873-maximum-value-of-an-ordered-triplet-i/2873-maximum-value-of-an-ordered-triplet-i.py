class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Input: an array of integers nums
        # Output: an integer with the maximum value over all triplets of indices


        # Algorithm: Burute Force
        # O(n^3)

        # res = 0
        # N = len(nums)

        # # Iterate through all possible j indices
        # for j in range(1, N - 1):
        #     # Find the maximum value to the left of j
        #     max_left = 0
        #     for i in range(j):
        #         max_left = max(max_left, nums[i])

        #     # Find the maximum value to the right of j
        #     max_right = 0
        #     for k in range(j + 1, N):
        #         max_right = max(max_right, nums[k])

        #     # Calculate the triplet value and update res
        #     value = (max_left - nums[j]) * max_right
        #     res = max(res, value)

        # # Return the final result
        # return res if res > 0 else 0


        # Algorithm: Gredy
        # O(n^2)

        # res = 0
        # N = len(nums)
        # left = nums[0]

        # for j in range(1, N):
        #     if nums[j] > left:
        #         left = nums[j]
        #     for k in range(j + 1, N):
        #         res = max(res, (left - nums[j]) * nums[k])
        # return res


        # Algorithm:
        # O(n)

        # res = 0
        # N = len(nums)

        # # Pre-calculate left
        # left = [0] * N
        # left[0] = nums[0]
        # for i in range(1, N):
        #     left[i] = max(left[i - 1], nums[i])

        # # Pre-calculate right
        # right = [0] * N
        # right[N - 1] = nums[N - 1]
        # for i in range(N - 2, -1, -1):
        #     right[i] = max(right[i + 1], nums[i])

        # # Calculate max tiplet value
        # for j in range(1, N - 1):
        #     res = max(res, (left[j - 1] - nums[j]) * right[j + 1])
        # return res if res > 0 else 0


        # Time Coplexity O(1)
        res = 0
        N = len(nums)

        # Track max left value
        max_left = nums[0]

        # Track max_right dynamically instead of using an array
        max_right = [0] * N
        max_right[N - 1] = nums[N - 1]

        for i in range(N - 2, 0, -1):
            max_right[i] = max(max_right[i + 1], nums[i])

        # Iterate through the middle element `j` while maintaining `max_left`
        for j in range(1, N - 1):
            res = max(res, (max_left - nums[j]) * max_right[j + 1])
            max_left = max(max_left, nums[j])

        return res if res > 0 else 0

