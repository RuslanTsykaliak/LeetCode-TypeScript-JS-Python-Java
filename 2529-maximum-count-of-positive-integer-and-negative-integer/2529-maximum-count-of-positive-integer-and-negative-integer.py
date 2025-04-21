class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Liner Sweep
        # max
        pos = 0
        neg = 0
        for n in nums:
            if n > 0:
                pos += 1
            if n < 0:
                neg += 1
        return max(pos, neg)
        