class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum_lr = 0
        len_lr = 0
        N = len(nums)
        c = 0
        l = 0
        for r in range(N):
            sum_lr += nums[r]
            len_lr += 1
        
            while sum_lr * len_lr >= k:
                sum_lr -= nums[l]
                len_lr -= 1
                l += 1
            c += len_lr
        return c