class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            if nums[i] > k:
                found = False
                for j in range(i):
                    if nums[i] == nums[j]:
                        found = True
                        break
                if not found:
                    res += 1
        return res

        