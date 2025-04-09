class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set()
        for n in nums:
            if n < k:
                return -1
            if n > k:
                unique.add(n)
        return len(unique)