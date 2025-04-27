class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = [0] * (len(nums) + 1)
        count[0] = 1
        total, res = 0, 0

        for v in nums:
            total += v & 1
            if total - k >= 0:
                res += count[total - k]
            count[total] += 1

        return res
