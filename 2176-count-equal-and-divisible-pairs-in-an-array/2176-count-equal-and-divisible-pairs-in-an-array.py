class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Input: An integer array nums and an integer k
        # Output: The number of index-pairs (i, j) with i < j, nums[i] == nums[j] and (i * j) % k == 0.

        # Algorithms: Brute Force. Nested loop
        count = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] != nums[j]:
                    continue
                if (i * j) % k == 0:
                    count += 1
        return count
        