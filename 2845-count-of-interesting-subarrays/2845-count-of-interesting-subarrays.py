class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int, {0: 1})
        for n in nums:
            if n % modulo == k:
                prefix = (prefix + 1) % modulo
            need = (prefix - k) % modulo
            count += freq[need]
            freq[prefix] += 1
        return count
