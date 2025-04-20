class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Algorithm: Greedy
        # Data Structure: Hash Map (Dictionary - collections.Counter)
        count = 0
        freq = Counter(answers)

        for key, value in freq.items():
            group_size = key + 1
            groups, remainder = divmod(value, group_size)
            count += groups * group_size
            if remainder:
                count += group_size

        return count