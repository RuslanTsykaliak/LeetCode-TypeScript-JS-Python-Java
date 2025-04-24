class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Nested loops
        # set for pre-subarray distinct tracking
        # Time Complexity O(n^2)
        # Space Complexity O(n)

        # count = 0
        # n = len(nums)
        # total_distinct = len(set(nums))
        # for i in range(n):
        #     current_distinct = set()
        #     for j in range(i, n):
        #         current_distinct.add(nums[j])
        #         if len(current_distinct) == total_distinct:
        #             count += 1
        # return count

        # Sliding Window
        # Dictionary freq to track window frequencies
        # Time Compexity O(n) because of singe pass
        # Space Complexity O(n)

        count = 0
        n = len(nums)
        total_distinct = len(set(nums))
        freq = {}
        left = 0
        for right, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
            while len(freq) == total_distinct:
                count += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        return count

        