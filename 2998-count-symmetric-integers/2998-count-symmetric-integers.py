from typing import List # Assuming List is imported if used elsewhere, not needed here

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0 # Initialize count of symmetric numbers

        # Check each number in the range [low, high]
        for i in range(low, high + 1):
            num_str = str(i) # Convert to string '1221'
            n = len(num_str) # Get number of digits, e.g., 4

            # Symmetric numbers must have even length
            if n % 2 != 0:
                continue # Skip odd length numbers

            # Calculate midpoint index, e.g., 4 // 2 = 2
            half_len = n // 2

            # Sum digits in first half, e.g., '12' -> 1+2=3
            left_sum = sum(int(d) for d in num_str[:half_len])
            # Sum digits in second half, e.g., '21' -> 2+1=3
            right_sum = sum(int(d) for d in num_str[half_len:])

            # If sums are equal, it's symmetric
            if left_sum == right_sum:
                count += 1 # Increment count

        return count # Return total count found