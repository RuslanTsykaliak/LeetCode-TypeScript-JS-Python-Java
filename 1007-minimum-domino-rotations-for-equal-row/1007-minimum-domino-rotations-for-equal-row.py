class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target):
            top, bottom = 0, 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return -1
                elif t != target:
                    top += 1
                elif b != target:
                    bottom += 1
            return min(top, bottom)
        
        res = check(tops[0])
        if res != -1 or tops[0] == bottoms[0]:
            return res
        return check(bottoms[0])