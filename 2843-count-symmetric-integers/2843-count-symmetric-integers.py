class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for i in range(low, high + 1):
            num_str = str(i)
            n = len(num_str)

            if n % 2 != 0:
                continue
            
            half_len = n // 2

            left_sum = sum(int(d) for d in num_str[:half_len])
            right_sum = sum(int(d) for d in num_str[half_len:])

            if left_sum == right_sum:
                res += 1
                
        return res
