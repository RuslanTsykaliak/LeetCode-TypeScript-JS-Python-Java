class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Array. Brute force. Nested Loop.
        # pairs = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             pairs += 1
        # return pairs

        # Hash Table
        freq = defaultdict(int)
        pairs = 0
        # For each number, the number of good pairs it forms
        # is equal to the count of the same number we have seen so far.
        for n in nums:
            pairs += freq[n]
            # After counting, we update its frequency
            freq[n] += 1
        return pairs

