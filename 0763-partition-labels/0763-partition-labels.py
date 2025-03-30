class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Algorithms: Two Pointers with HashMap & Greedy

        # 1. variables
        res = []
        start, end = 0, 0

        # 2. HashMap with the last index of the character
        # For example, a:2, b:3, c:5
        last_index = {char: idx for idx, char in enumerate(s)}

        # Iterate over the string
        for i, char in enumerate(s):
            end = max(end, last_index[char]) # end for a will be 2, end for b to 3

            if i == end:
                res.append(end - start + 1)
                start = i + 1
                
        return res




        