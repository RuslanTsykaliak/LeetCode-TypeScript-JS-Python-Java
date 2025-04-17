class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Agorithm: Brute Force

        # Input: array nums and an integer k
        # Output: Count
        # Coditions:
        # nums[i] == nums[j]
        # (i * j) is divisible by k

        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                # Just copy past explanation part
                if nums[i] != nums[j]: continue
                if (i * j) % k == 0:
                    count += 1
        return count
        