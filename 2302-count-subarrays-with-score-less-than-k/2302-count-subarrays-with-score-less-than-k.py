class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count, total, i = 0, 0, 0
        for j in range(len(nums)):
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            count += j - i + 1
        return count
