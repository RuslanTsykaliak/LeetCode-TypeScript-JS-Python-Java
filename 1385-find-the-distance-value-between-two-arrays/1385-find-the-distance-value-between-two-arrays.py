class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for x in arr1:
            noCloseNeighbor = True
            for y in arr2:
                if abs(x - y) <= d:
                    noCloseNeighbor = False
            if noCloseNeighbor:
                count += 1
        
        return count