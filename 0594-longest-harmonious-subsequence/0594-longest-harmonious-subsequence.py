class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, 1
        length = 0
        while r < len(nums):
            diff = nums[r] - nums[l]
            if diff == 1:
                length = max(length, r - l + 1)
            if diff <= 1:
                r += 1
            else:
                l += 1
        
        return length