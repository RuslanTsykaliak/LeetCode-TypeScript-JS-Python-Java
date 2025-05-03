class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(candid):
            # check O(N)
            merge_to_bottom = merge_to_top = 0
            for i in range(n):
                if tops[i] != candid and bottoms[i] != candid:
                    return -1
                elif tops[i] != candid:
                    merge_to_top += 1
                elif bottoms[i] != candid:
                    merge_to_bottom += 1
            return min(merge_to_top, merge_to_bottom)
        
        n = len(tops)
        rotations = check(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check(bottoms[0])