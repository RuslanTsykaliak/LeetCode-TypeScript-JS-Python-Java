class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Two Pointers
        result = 0
        n = len(nums)

        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
            right[n - i - 1] = right[n - i] + nums[n - i]
        
        for i in range(n):
            if nums[i] != 0:
                continue
            if left[i] == right[i]:
                result += 2
            if abs(left[i] - right[i]) == 1:
                result += 1
        
        return result