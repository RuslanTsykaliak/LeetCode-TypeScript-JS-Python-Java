class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # counts of each normalized domino key
        freq = [0] * 100      
        total = 0

        for x, y in dominoes:
            key = x * 10 + y if x <= y else y * 10 + x
            total += freq[key]
            freq[key] += 1

        return total
