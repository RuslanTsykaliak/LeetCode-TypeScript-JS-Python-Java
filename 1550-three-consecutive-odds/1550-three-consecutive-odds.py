class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Algorithm: Iterative Counting
        # Data Structures: List/Array
        # Time Complexity O(n)
        # Space Complexity O(1)

        if len(arr) < 3:
            return False
        
        consecutiveOddCount = 0

        for n in arr:
            if n % 2 != 0:
                consecutiveOddCount += 1
                if consecutiveOddCount == 3:
                    return True
            else:
                consecutiveOddCount = 0
        
        return False