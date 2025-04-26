class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        minKIdx = maxKIdx = outOfBoundsIdx = -1

        for i, v in enumerate(nums):
            # reset on invalid value
            if v < minK or v > maxK:
                outOfBoundsIdx = i

            # update last seen positions
            if v == minK:
                minKIdx = i
            if v == maxK:
                maxKIdx = i

            # earliest start that includes both minK and maxK
            validStart = min(minKIdx, maxKIdx)
            count += max(0, validStart - outOfBoundsIdx)

        return count