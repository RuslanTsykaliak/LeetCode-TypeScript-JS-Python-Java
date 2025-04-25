class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for length in range(l, r + 1):
            if length > n:
                continue
            
            window_sum = sum(nums[:length])
            if window_sum > 0:
                min_sum = min(min_sum, window_sum)

            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)
        
        return min_sum if min_sum < float('inf') else -1