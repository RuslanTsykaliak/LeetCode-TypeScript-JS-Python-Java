class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            good = True
            if i - k >= 0:
                if nums[i] <= nums[i - k]:
                    good = False
            if i + k < n:
                if nums[i] <= nums[i + k]:
                    good = False
            if good:
                count += nums[i]
        return count
        