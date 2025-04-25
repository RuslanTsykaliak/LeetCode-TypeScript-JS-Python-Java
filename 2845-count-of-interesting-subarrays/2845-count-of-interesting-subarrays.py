class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Prefix Sum
        # Hash Map
        # Time Complexity O(n)
        # Space Complexity O(min(n, modulo))
        count = 0
        prefix_mod = 0
        mod_freq = {0: 1}

        for num in nums:
            if num % modulo == k:
                prefix_mod = (prefix_mod + 1) % modulo
            needed = (prefix_mod - k) % modulo
            count += mod_freq.get(needed, 0)
            mod_freq[prefix_mod] = mod_freq.get(prefix_mod, 0) + 1
            
        return count
        