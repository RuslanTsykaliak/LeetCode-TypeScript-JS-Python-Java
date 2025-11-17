class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if idx != -1 and i - idx - 1 < k:
                    return False
                idx = i
        return True