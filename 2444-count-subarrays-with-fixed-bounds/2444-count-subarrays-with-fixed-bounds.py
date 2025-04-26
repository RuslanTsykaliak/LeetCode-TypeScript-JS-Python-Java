class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        # Positions of the last seen minK, maxK, and any out-of-range value
        min_i = max_i = last_i = -1

        for i, n in enumerate(nums):
            # Update last seen positions
            if n == minK:
                min_i = i
            if n == maxK:
                max_i = i

            # If n is outside [minK, maxK], no subarray crossing i can be valid
            if not (minK <= n <= maxK):
                last_i = i

            # Earliest index where both minK and maxK are included in [s..i]
            valid_start = min(min_i, max_i)
            # All start positions s in (last_i .. valid_start] yield valid subarrays ending at i
            if valid_start > last_i:
                count += valid_start - last_i

        return count