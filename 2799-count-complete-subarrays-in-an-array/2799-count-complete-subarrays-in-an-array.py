class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Input: An array 'nums' of positive integers (e.g., [1, 2, 3, ...])
        # Output: The count of subarrays where the number of distinct elements in the subarray
        #         matches the number of distinct elements in the entire array.
        #         A subarray is a contiguous, non-empty part of the array.

        # Optimized Sliding Window Approach:
        # Instead of checking all subarrays, use a sliding window to maintain a window of elements
        # and count subarrays efficiently. The idea is to expand the window until it contains all
        # distinct elements, then count valid subarrays ending at the current position, and shrink
        # the window when needed to find more valid subarrays.

        total_distinct = len(set(nums))  # Total unique elements in the array
        # Example: For nums = [1, 3, 1, 2, 2], total_distinct = 3 (elements: 1, 2, 3)
        count = 0  # Counter for complete subarrays
        n = len(nums)  # Length of the input array
        freq = {}  # Dictionary to store frequency of elements in current window
        distinct_in_window = 0  # Track number of distinct elements in current window
        left = 0  # Left pointer of the sliding window

        # Single pass: Iterate over the array with right pointer to expand window
        for right in range(n):
            # Add the current element to frequency map
            if nums[right] not in freq:
                freq[nums[right]] = 1
                distinct_in_window += 1  # New distinct element added
            else:
                freq[nums[right]] += 1

            # Shrink window from left while we have all distinct elements
            # This helps count all valid subarrays ending at 'right'
            while distinct_in_window == total_distinct and left <= right:
                # All subarrays from 'left' to 'right' and beyond (up to end of array)
                # are valid because adding more elements won't reduce distinct count
                count += n - right  # Add number of subarrays ending at 'right'
                # Example: nums = [1, 3, 1, 2], at right=3, window=[1,3,1,2], distinct=3
                # If n=5, count += 5-3=2 (subarrays [1,3,1,2] and [1,3,1,2,2])

                # Shrink window by removing element at 'left'
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]  # Remove element if frequency becomes 0
                    distinct_in_window -= 1  # Decrease distinct count
                left += 1  # Move left pointer forward

        return count  # Return total count of complete subarrays