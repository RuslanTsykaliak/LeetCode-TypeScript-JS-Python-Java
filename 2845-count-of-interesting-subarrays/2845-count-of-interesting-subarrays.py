class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Prefix Sum with Hash Map

        current_remainder = 0
        interesting_subarrays = 0
        remainder_counter = {0: 1}

        for n in nums:
            if n % modulo == k:
                current_remainder = (current_remainder + 1) % modulo
            need = (current_remainder - k) % modulo
            interesting_subarrays += remainder_counter.get(need, 0)

            remainder_counter[current_remainder] = (remainder_counter.get(current_remainder, 0) + 1)

        return interesting_subarrays
