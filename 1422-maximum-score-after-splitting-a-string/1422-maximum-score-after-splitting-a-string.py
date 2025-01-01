class Solution:
    def maxScore(self, s: str) -> int:
        result = zeroes = 0
        ones = s.count("1")

        for item in s[:-1]:
            if item == "0":
                zeroes += 1
            else:
                ones -= 1

            result = max(result, ones + zeroes)

        return result
