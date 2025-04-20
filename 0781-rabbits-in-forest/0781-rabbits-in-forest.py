class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Input: answers - list of counts of other same-color rabbits
        # Output: Minimum total rabbits in the forest

        # Algorithm: Greedy
        # Data Structure: Hash Map
        # Time: O(N) | Space: O(U) unique answers

        count = 0 # Initialize total minimum rabbit count
        # Count frequency of each answer value provided: O(N) time
        freq = Counter(answers)

        # Iterate through each unique answer (key) and its frequency (value): O(U) iterations
        for key, value in freq.items():
            # If rabbit answers 'key', it implies group size = 'key + 1'
            group_size = key + 1

            # Calc full groups & leftover rabbits for this answer freq
            # divmod(value, group_size) returns (value // group_size, value % group_size)
            groups, remainder = divmod(value, group_size)

            # Add rabbits accounted for by the fully represented groups
            count += groups * group_size

            # If there are leftover rabbits (remainder > 0)...
            if remainder:
                # ...they require one more complete group of 'group_size'
                count += group_size

        return count