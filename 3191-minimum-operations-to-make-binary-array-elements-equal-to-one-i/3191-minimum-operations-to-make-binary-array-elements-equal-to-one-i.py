class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Greedy approach
        # Time Complexity: O(n)
        # Space Complexity: O(1) (in-place)

        # Input: A binary array (e.g., [0, 1, 1, 0, ...])
        # Output: The minimum number of operations to make all elements 1, or -1 if impossible.
        # Restriction: In one operation, we can choose any 3 consecutive elements and flip them (0 → 1, 1 → 0).
        # Idea:
        # - Loop through the array.
        # - When we find a 0 at position i, flip the next 3 elements (i, i+1, i+2).
        # - Count each flip operation.
        # - After all flips, check if all elements are 1.
        #   - If yes, return the count.
        #   - If no, return -1.

        res = 0
        n = len(nums)

        def flip_three(nums, j):
            # Flip 3 consecutive elements starting at index j
            for i in range(j, min(j + 3, n)):
                nums[i] = 0 if nums[i] == 1 else 1

        # Traverse the array
        for i in range(n - 2):  # n - 2 because we need room for 3 elements
            if nums[i] == 0:
                flip_three(nums, i)
                res += 1

        # Check if all elements are 1
        if all(num == 1 for num in nums):
            return res
        else:
            return -1
