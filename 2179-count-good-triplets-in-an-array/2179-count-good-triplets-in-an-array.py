class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Algorithm Pattern: Reverse Iteration with Binary Search
        count = 0

        # Data Structure: Array 'indices'
        # Purpose: Map each number in nums1 to its index so we can transform nums2.
        indices = [0] * len(nums1)
        for i, num in enumerate(nums1):
            indices[num] = i

        # Transform nums2:
        # Replace each number in nums2 with its corresponding index from nums1.
        # Now, nums2 (stored in nums1) represents the order of numbers in terms of their positions from nums1.
        for i, num in enumerate(nums2):
            nums1[i] = indices[num]

        # Data Structure: SortedList 'arr'
        # Purpose: Maintain a dynamically sorted list to allow fast binary search.
        # This helps us count how many numbers are less than the current one efficiently.
        arr = SortedList()

        # Process the transformed array in reverse order. For each number, determine the count of valid elements
        # on its left and right (in the transformed world) that can form a good triplet.
        for i, num in enumerate(nums1[::-1]):
            idx = arr.bisect(num)  # Count numbers in 'arr' that are smaller than 'num'
            # The expression (i - idx) calculates the count of numbers seen so far that are greater than 'num'.
            # Multiplying this with (num - idx) combines the counts on both sides.
            count += (i - idx) * (num - idx)
            arr.add(
                num
            )  # Add the current number to the SortedList for future comparisons

        return count
