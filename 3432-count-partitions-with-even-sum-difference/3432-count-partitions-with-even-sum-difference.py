class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums) % 2 == 0:
            return len(nums) - 1
        else:
            return 0