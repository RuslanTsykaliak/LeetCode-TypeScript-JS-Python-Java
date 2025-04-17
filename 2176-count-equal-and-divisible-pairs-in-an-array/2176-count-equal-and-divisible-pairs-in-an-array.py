class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Input: An integer array nums and an integer k
        # Output: The number of index-pairs (i, j) with i < j, nums[i] == nums[j] and (i * j) % k == 0.

        # Algorithms: Brute Force. Nested loop
        # Time Complexity O(n^2)
        # count = 0
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] != nums[j]:
        #             continue
        #         if (i * j) % k == 0:
        #             count += 1
        # return count

        # Algorithms: Single Pass. Hash Table
        # Time Complexity O(n)
        count = 0
        index_map = defaultdict(list)
        for j, num in enumerate(nums):
            for i in index_map[num]:
                if (i * j) % k == 0:
                    count += 1
            index_map[num].append(j)
        return count
        