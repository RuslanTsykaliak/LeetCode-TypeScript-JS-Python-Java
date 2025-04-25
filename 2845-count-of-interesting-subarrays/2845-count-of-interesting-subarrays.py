class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = 0
        count = 0
        mp = {}
        mp[0] = 1

        for ele in nums:
            if ele%modulo == k:
                prefix += 1
                prefix = prefix%modulo
            count += mp.get((prefix-k)%modulo, 0)
            mp[prefix] = mp.get(prefix, 0) + 1
        return count