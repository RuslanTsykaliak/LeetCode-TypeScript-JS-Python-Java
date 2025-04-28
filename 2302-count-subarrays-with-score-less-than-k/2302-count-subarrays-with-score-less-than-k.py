class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        window = 0
        left = 0
        count = 0

        for right in range(len(nums)):
            total += nums[right]
            window += 1
        
            while total * window >= k:
                total -= nums[left]
                window -= 1
                left += 1
            count += window
        return count