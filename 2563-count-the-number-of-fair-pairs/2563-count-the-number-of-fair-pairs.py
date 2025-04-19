class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        fairCount = self.countPairs(nums, upper) - self.countPairs(nums, lower - 1)
        return fairCount

    def countPairs(self, nums, target):
        count = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] <= target:
                count = count + (r - l)
                l = l + 1
            else:
                r = r - 1
        return count