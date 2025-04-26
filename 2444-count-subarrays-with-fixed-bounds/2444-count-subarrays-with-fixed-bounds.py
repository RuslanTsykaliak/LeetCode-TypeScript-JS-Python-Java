class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Sliding Window
        # Time Complexity O(n)
        # Space Complexity O(1)
        count = 0

        min_i = max_i = last_i = -1

        for i, n in enumerate(nums):
            if n == minK:
                min_i = i
            if n == maxK:
                max_i = i

            if not (minK <= n <= maxK):
                last_i = i
            
            valid_start = min(min_i, max_i)
            if valid_start > last_i:
                count += valid_start - last_i

        return count