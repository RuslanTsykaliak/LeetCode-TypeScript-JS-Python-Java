class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Input: an integer array
        # Output: number of steps to make the array have all elements distinct (Unique)
        # Rules: we can remove 3 elements from the beginning of thee array. If the array has fewer than 3 elements, remove all remaining elements
        
        seen = [False] * 101

        for i in range(len(nums) -1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            else:
                seen[nums[i]] = True
        return 0
