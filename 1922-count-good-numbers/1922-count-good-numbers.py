class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Define the large prime modulus (spy math number!)
        MOD = 10**9 + 7

        # Determine counts for even/odd index positions in the code
        num_even_indices = (n + 1) // 2  # Count of slots 0, 2, 4...
        num_odd_indices = n // 2  # Count of slots 1, 3, 5...

        # Calculate combinations for even positions (5 symbol choices each)
        # Use pow(base, exp, mod) for efficient modular exponentiation
        even_pos_choices = pow(5, num_even_indices, MOD)

        # Calculate combinations for odd positions (4 symbol choices each)
        odd_pos_choices = pow(4, num_odd_indices, MOD)

        # Total combinations = (even choices) * (odd choices)
        # Compute the final result modulo MOD to keep numbers manageable
        return (even_pos_choices * odd_pos_choices) % MOD
