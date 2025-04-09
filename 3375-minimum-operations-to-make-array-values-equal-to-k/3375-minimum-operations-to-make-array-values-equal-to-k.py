class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = set()

        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            h.add(nums[i])
        return len(h) - 1 if k in h else len(h)


        