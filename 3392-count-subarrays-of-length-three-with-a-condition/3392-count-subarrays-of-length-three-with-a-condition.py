class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # Input: an array of integers
        # Output: an integer
        # Conditions: 
        # 1. count subarrays of length 3
        # 2. sum of 1 and 3 element equal half of the second element

        # # Brute Force
        # count = 0

        # # we start the loop from 3 element
        # for i in range(2, len(nums)):
        #     # check if the first and second element 
        #     # equal half of 2 element
        #     if nums[i] + nums[i - 2] == nums[i - 1] / 2:
        #         count += 1

        # return count

        # Sliding Window
        count = 0
        # l represent the most left 0 window part 
        for l in range(len(nums) - 2): # short search by 2
            # right represent righ element with 2 steps from left
            r = l + 2
            # middle represent the element betwen left and right
            m = l + 1
            if nums[l] + nums[r] == nums[m] / 2:
                count += 1
        
        return count



        