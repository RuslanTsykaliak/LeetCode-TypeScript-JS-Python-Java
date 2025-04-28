class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Algorithm: Slidig Window
        total = 0        # sum of elements in the current window [left…right]
        window = 0       # length of the current window
        left = 0         # left boundary of our sliding window
        count = 0        # total number of valid subarrays

        for right in range(len(nums)):
            # include the element at index `right`
            total += nums[right]
            window += 1

            # shrink from the left until the score < k
            # score = total * window
            while total * window >= k:
                total -= nums[left]
                window -= 1
                left += 1

            # all subarrays ending at `right` with lengths 1…window are valid
            count += window

        return count
