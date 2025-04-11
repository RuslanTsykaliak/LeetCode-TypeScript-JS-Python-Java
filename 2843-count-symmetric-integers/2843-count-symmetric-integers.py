class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n: int) -> bool:
            digits = list(map(int, str(n)))
            length = len(digits)
            if length % 2 != 0:
                return False
            half = length // 2
            return sum(digits[:half]) == sum(digits[half:])
        
        return sum(is_symmetric(x) for x in range(low, high + 1))
        