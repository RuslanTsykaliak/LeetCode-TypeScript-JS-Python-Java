class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        sym_sum = 0

        for i in range(low, high + 1):
            num = str(i)
            if len(num) % 2 != 0:
                continue

            n = len(num) // 2

            if sum(int(d) for d in num[:n]) == sum(int(d) for d in num[n:]):
                sym_sum += 1

        return sym_sum
