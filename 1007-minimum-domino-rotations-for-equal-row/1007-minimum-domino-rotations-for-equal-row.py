class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Algorithm: Greedy
        # Time Complexity O(n)
        # Space Complexity O(1)

        def check(target: int) -> int:
            top_flips, bottom_flips = 0, 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return -1
                if t != target:
                    top_flips += 1
                elif b != target:
                    bottom_flips += 1
            return min(top_flips, bottom_flips)
        
        res = check(tops[0])
        if res != -1 or tops[0] == bottoms[0]:
            return res
        return check(bottoms[0])