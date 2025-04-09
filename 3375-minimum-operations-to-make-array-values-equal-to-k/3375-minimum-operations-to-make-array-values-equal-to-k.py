class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # HashSet. Greedy

        # If any number is smaller than k, we return -1
        if min(nums) < k:
            return -1
        
        uniqueHeights = set()

        # We check all numbers in the array nums 
        for n in nums:
            # Only track values that are greater than k
            if n > k:
                uniqueHeights.add(n)
        # Each unique height above k will need the spell to reduce
        return len(uniqueHeights)
        