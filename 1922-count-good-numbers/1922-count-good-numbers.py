class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        num_even_indices = (n + 1) // 2
        num_odd_indices = n // 2

        even_pos_choices = pow(5, num_even_indices, MOD)
        odd_pos_choices = pow(4, num_odd_indices, MOD)

        return (even_pos_choices * odd_pos_choices) % MOD
        