class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        num_even_indices = (n + 1) // 2
        num_odd_indices = n // 2
        even_pos_choices = pow(5, num_even_indices, MOD)
        odd_pos_choices = pow(4, num_odd_indices, MOD)
        return (even_pos_choices * odd_pos_choices) % MOD

        # res = 1
        # rem = n % 2
        # n -= rem
        # res = pow(20, n // 2, 10**9 + 7)
        # if rem == 1:
        #     res *= 5
        # return res % (10**9 + 7)

