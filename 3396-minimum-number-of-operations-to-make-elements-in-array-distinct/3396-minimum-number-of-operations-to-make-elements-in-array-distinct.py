class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Algorithm: Reverse Traversal. HashSet
        # Time Complexity O(n)
        # Space Complexity O(n)
        seen = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return (i // 3) + 1
            else:
                seen.add(nums[i])
        return 0
        