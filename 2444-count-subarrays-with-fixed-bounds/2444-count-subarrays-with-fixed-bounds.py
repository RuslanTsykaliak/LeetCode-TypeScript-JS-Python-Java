class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Sliding Window
        # Time Complexity O(n)
        # Space Complexity O(1)
        count = 0

        minKIdx = maxKIdx = outOfBoundsIdx = -1

        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                outOfBoundsIdx = i
            if v == minK:
                minKIdx = i
            if v == maxK:
                maxKIdx = i
            
            validStart = min(minKIdx, maxKIdx)
            count += max(0, validStart - outOfBoundsIdx)

        return count
        