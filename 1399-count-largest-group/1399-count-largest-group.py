class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Input: an integer n
        # Output: the number of groups that have the largest size
        # Conditions: we count the size of group based on added values of separate numbers: [1, 10] = 1 = 10 = 1 + 0; [2,11] = 2 = 11 = 1 + 1; 
        # However, the size of group is different [1, 13] has size of 2 while [9] has the size of one

        # Algorithm: Hash Map
        # Time and Space Complexity O(n)

        # Create a dictionary to count the frequency for each digit sum
        freq = defaultdict(int)

        # Iterate for all numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Compute the sum of the digits of i
            digit_sum = sum(int(digit) for digit in str(i))
            # Increment the frequency for this digit sum
            freq[digit_sum] += 1

        # Find the maximum frequency among the groups
        max_freq = max(freq.values())

        # Count the number of groups that have the maximum frequency
        return sum(1 for group in freq.values() if group == max_freq)
