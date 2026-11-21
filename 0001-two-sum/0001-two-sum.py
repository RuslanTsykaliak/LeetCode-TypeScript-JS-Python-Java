class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Input: array of integers and one integer
        # Outpout: array with two indices
        # Process: calculate two integers in the array that sum to the target integer

        # Nested loop - we will check all elements by taking the first element and adding all other elements to it and compare to target, and loop through whole array until the results found.

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j