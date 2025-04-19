class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binSearch(l, r, t):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= t:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        nums.sort()
        res = 0
        for i in range(len(nums)):
            lo = lower - nums[i]
            up = upper - nums[i]
            res += binSearch(i + 1, len(nums) - 1, up + 1) - binSearch(
                i + 1, len(nums) - 1, lo
            )
        return res
