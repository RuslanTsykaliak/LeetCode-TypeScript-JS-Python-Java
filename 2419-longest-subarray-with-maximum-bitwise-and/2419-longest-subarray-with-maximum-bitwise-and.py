class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = res = current_streak = 0
        for n in nums:
            if max_val < n:
                max_val = n
                res = current_streak = 0
            
            if max_val == n:
                current_streak += 1
            else:
                current_streak = 0
            
            res = max(res, current_streak)
        return res