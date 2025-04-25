class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int, {0: 1})

        for n in nums:
            if n % modulo == k:
                prefix += 1
                prefix = prefix % modulo
            count += freq.get((prefix - k) % modulo, 0)
            freq[prefix] = freq.get(prefix, 0 ) + 1

        return count
        