class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window
        # Input: array nums of positive integers and integer k
        # Output: integer
        # Conditions:
        # count subarrays where maximum integer of nums appears at least k times
        # 1. we need to know maximum integer in the nums array
        # 2. the maximum integer should be present k times
        # 3. we should slide the window and increment count each time the window
        # satisfies conditions

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
            
            count += left  # All subarrays ending at right and starting before left are valid

        return count

        