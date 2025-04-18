class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        good_freqs = set()
        
        # Helper: Convert frequency dictionary to a tuple for digits 0 to 9.
        def freq_to_tuple(freq):
            return tuple(freq.get(str(d), 0) for d in range(10))
        
        # Depending on the parity of n, the palindrome is built differently.
        palindromes = []
        if n == 1:
            # Single digit palindromes (1 to 9)
            for d in range(1, 10):
                p = d
                if p % k == 0:
                    freq = Counter(str(p))
                    good_freqs.add(freq_to_tuple(freq))
        else:
            # n >= 2
            half_len = n // 2
            # For even n: palindrome = half + reverse(half)
            # For odd n:  palindrome = half + middle + reverse(half)
            # Generate first half digits (first digit cannot be '0')
            from itertools import product
            digits = '0123456789'
            first_half_range = product(digits, repeat=half_len)
            
            # A helper function to build a palindrome string from half and optional middle.
            def build_palindrome(half, middle=""):
                return "".join(half) + middle + "".join(reversed(half))
            
            # If n is even
            if n % 2 == 0:
                for half in first_half_range:
                    if half[0] == '0':
                        continue  # leading zero not allowed for n-digit number
                    pal_str = build_palindrome(half)
                    p = int(pal_str)
                    if p % k == 0:
                        freq = Counter(pal_str)
                        good_freqs.add(freq_to_tuple(freq))
            else:
                # n odd: need to iterate middle digit from '0' to '9'
                # Reset first_half_range because product iterator was exhausted.
                first_half_range = product(digits, repeat=half_len)
                for half in first_half_range:
                    if half[0] == '0':
                        continue
                    for m in digits:
                        pal_str = build_palindrome(half, m)
                        # Ensure that overall string length is n (leading zero is already controlled).
                        if len(pal_str) != n:
                            continue
                        p = int(pal_str)
                        if p % k == 0:
                            freq = Counter(pal_str)
                            good_freqs.add(freq_to_tuple(freq))
        
        # Now, for each unique frequency multiset, calculate the number of distinct rearrangements.
        total_count = 0
        for freq_tuple in good_freqs:
            # Convert the tuple (counts for digits 0..9) to a list for easier access.
            counts = list(freq_tuple)
            # Calculate total number of distinct permutations:
            total_perm = factorial(n)
            for count in counts:
                total_perm //= factorial(count)
            
            # Calculate number of invalid permutations with a leading zero.
            if counts[0] > 0:
                # We fix a zero at the first position; now arrange the remaining n-1 positions.
                invalid_perm = factorial(n - 1)
                # Adjust count for digit '0' because one zero is already used.
                remaining_counts = counts.copy()
                remaining_counts[0] -= 1
                for count in remaining_counts:
                    invalid_perm //= factorial(count)
            else:
                invalid_perm = 0
            
            valid_perm = total_perm - invalid_perm
            total_count += valid_perm
        
        return total_count