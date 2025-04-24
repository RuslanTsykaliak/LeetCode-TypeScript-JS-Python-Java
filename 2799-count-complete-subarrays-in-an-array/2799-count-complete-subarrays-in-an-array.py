class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Nested loops
        # set for pre-subarray distinct tracking
        # Time Complexity O(n^2)
        # Space Complexity O(n)

        count = 0
        n = len(nums)
        total_distinct = len(set(nums))
        for i in range(n):
            current_distinct = set()
            for j in range(i, n):
                current_distinct.add(nums[j])
                if len(current_distinct) == total_distinct:
                    count += 1
        return count

        