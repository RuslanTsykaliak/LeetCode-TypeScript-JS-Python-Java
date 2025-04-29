class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window
        # Time Complexity O(n)
        # Space Complexity O(1)

        count = 0
        top = max(nums)
        left = 0
        window = 0

        for right in range(len(nums)):
            if nums[right] == top:
                window += 1
            
            while window >= k:
                if nums[left] == top:
                    window -= 1
                left += 1

            count += left

        return count