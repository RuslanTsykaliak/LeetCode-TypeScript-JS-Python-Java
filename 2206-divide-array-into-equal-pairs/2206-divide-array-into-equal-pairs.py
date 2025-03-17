class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # What is the input? An array of integers.
        # What is the output? True if all integers in the array can be paired with equal integers.
        # For example, input [3, 2, 2, 3] outputs True because (3, 3) and (2, 2) are equal pairs.

        # Store result
        res = False

        # Check if the input array has an even number of integers; if not, return False.
        if len(nums) % 2 != 0:
            return res

        # How can we check if all elements have equal pairs?

        # Sort the array and check elements by comparing pairs of indexes.
        # For example, in an array with 4 elements, check if indexes 0 and 1 are equal,
        # and if indexes 2 and 3 are equal. If all pairs are equal, return True.
        # Otherwise, return False.
        # Space Complexity: O(1)
        nums.sort()

        # Iterate through the array to check paired elements
        for i in range(0, len(nums), 2):
            j = i + 1
            if nums[i] == nums[j]:
                res = True
            else:
                return False  # Directly return False when a mismatch is found

        return res

        # Alternatively, we can use a queue:
        # Add elements to the queue, and remove them in pairs.
        # If by the end the queue is empty, return True.
        # If something remains, return False.
        # Space Complexity: O(n) because we create additional storage for the queue.
