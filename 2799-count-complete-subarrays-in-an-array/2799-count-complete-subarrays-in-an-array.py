class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Input: An array 'nums' filled with positive integers (e.g., [1, 2, 3, ...])
        # Output: The count of subarrays where the number of distinct elements in the subarray
        #         is equal to the number of distinct elements in the entire array.
        #         A subarray is a contiguous part of the array.

        # Example to illustrate subarrays using nums = [5, 5, 5, 5] with their indices:
        # Starting at index 0: [0] -> [5]
        #                      [0,1] -> [5,5]
        #                      [0,1,2] -> [5,5,5]
        #                      [0,1,2,3] -> [5,5,5,5]
        # Starting at index 1: [1] -> [5]
        #                      [1,2] -> [5,5]
        #                      [1,2,3] -> [5,5,5]
        # Starting at index 2: [2] -> [5]
        #                      [2,3] -> [5,5]
        # Starting at index 3: [3] -> [5]
        # Total number of possible subarrays: 10
        # In this case, distinct elements in the whole array = 1 (only 5),
        # so all 10 subarrays are "complete" since each has 1 distinct element.

        # Brute Force Approach:
        # We will generate all possible subarrays and check if the number of distinct
        # elements in each subarray matches the total distinct elements in the array.
        count = 0
        n = len(nums)
        # Calculate the total number of unique elements in the entire array
        # For example, if nums = [1, 2, 1, 3], total_distinct = 3 (1, 2, 3)
        total_distinct = len(set(nums))
        for i in range(n):
            # Initialize an empty set to store distinct elements in the current subarray
            current_distinct = set()
            # Iterate over all possible endings for subarrays starting at index i
            # Goal: Check if the subarray from index i to j has the same number of
            # distinct elements as the entire array. If yes, increment count.
            # For example, in nums = [1, 2, 1, 3], if i=0 and j=3, subarray = [1,2,1,3]
            # has 3 distinct elements (1,2,3), which matches total_distinct, so count += 1
            for j in range(i, n):
                current_distinct.add(nums[j])
                if len(current_distinct) == total_distinct:
                    count += 1
        return count