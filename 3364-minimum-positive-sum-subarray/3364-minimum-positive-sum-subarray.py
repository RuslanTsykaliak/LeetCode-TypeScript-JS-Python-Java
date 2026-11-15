class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # We are given array and start and end of the array, perfect sliding window
        # The goal is to find minimal positive sum that is between all possible combination between minimal lenght l and max length r

        n = len(nums) # Length of the array
        min_sum = float('inf') # Positive infinitive float meaning integer with decemals

        for length in range(l, r + 1):
            if length > n: # check if provided boundaries are not outside of array length
                continue
            
            window_sum = sum(nums[:length])
            if window_sum > 0: # second check if array range isn't negative number or 0
                min_sum = min(min_sum, window_sum) # we update min_sum fir time after checking the first possible range
            
            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]
                if window_sum > 0: # third check for netative number or 0
                    min_sum = min(min_sum, window_sum)
        
        return min_sum if min_sum < float('inf') else -1 # 


