class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        count = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == min_k:
                min_i = i
            if x == max_k:
                max_i = i
            if not min_k <= x <= max_k:
                i0 = i
            j = min_i if min_i < max_i else max_i
            if j > i0:
                count += j - i0
        return count
