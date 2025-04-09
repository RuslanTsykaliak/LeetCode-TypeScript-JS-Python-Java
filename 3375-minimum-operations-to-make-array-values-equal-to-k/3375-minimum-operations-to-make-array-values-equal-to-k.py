class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        uniqueHeights = set()
        
        for n in nums:
            if n > k:
                uniqueHeights.add(n)
        
        return len(uniqueHeights)