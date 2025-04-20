class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Input: an array of integers
        # Output: return the minimum number of rabbits that could be in the forest based on their answers – accouting for both answering and unseen rebbits of the same color.
        # Algorithm: Greedy

        count = 0
        d = {}
        for i in answers:
            
            if i == 0:
                count += 1
            else:
                if i not in d or i == d[i]:
                    d[i] = 0
                    count += 1 + i
                else:
                    d[i] += 1

        return count

        