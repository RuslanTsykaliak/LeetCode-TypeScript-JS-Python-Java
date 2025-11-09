class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        
        while num1 and num2:
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res