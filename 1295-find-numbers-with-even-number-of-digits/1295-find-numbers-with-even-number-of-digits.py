class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Input: integer array list
        # Ouput: integer
        # Constrains:
        # 1. find integers that contian an even number of digits
        # 2. count them

        count = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count
        