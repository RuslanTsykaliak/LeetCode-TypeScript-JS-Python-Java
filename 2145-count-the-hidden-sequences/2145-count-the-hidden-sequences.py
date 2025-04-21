class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Beats 62.63%
        # x = y = cur = 0
        # for d in differences:
        #     cur += d
        #     x = min(x, cur)
        #     y = max(y, cur)
        #     if y - x > upper - lower:
        #         return 0
        # return (upper - lower) - (y - x) + 1

        #### Beats 92.93%
        # pfs = list(accumulate(differences, initial = 0))
        # return max(0, upper - lower - max(pfs) + min(pfs) + 1)

        #### Beats 94.95%

        # lowest = 0
        # highest = 0
        # current = 0
        # for i in differences:
        #     current += i
        #     if lowest > current:
        #         lowest = current
        #     if highest < current:
        #         highest = current
        # differences_range = highest - lowest
        # given_range = upper - lower
        # res = (given_range - differences_range + 1)
        # if res > 0:
        #     return res
        # else:
        #     return 0

        #### Beats 48.48%
        # Track prefix‐sum extremities (relative to hidden[0])
        # lowest = highest = curr = 0
        # for d in differences:
        #     curr += d
        #     lowest = min(lowest, curr)
        #     highest = max(highest, curr)

        # # The hidden sequence spans a range of (highest – lowest).
        # # We can slide that range inside [lower, upper]:
        # span = highest - lowest
        # full_range = upper - lower

        # # Number of valid starting values = (full_range – span + 1), floored at 0
        # return max(0, full_range - span + 1)


        #### 35.35 %
        # min_val = max_val = curr = 0
        # for diff in differences:
        #     curr += diff
        #     min_val = min(min_val, curr)
        #     max_val = max(max_val, curr)

        # required_range = max_val - min_val
        # available_range = upper - lower
        # possible_starts = available_range - required_range + 1

        # return max(0, possible_starts)

        #### 95.96%
        # lowest = highest = current = 0
        # for diff in differences:
        #     current += diff
        #     if current < lowest:
        #         lowest = current
        #     if current > highest:
        #         highest = current
        
        # differences_range = highest - lowest
        # given_range = upper - lower
        # res = (given_range - differences_range + 1)

        # return max(0, res)

        #### 86.87
        # current = min_sum = max_sum = 0
        # for d in differences:
        #     current += d
        #     if current < min_sum:
        #         min_sum = current
        #     if current > max_sum:
        #         max_sum = current
        # range_ = max_sum - min_sum
        # available = (upper - lower) - range_ + 1
        # return max(0, available)

        ####
        lowest = highest = current = 0
        for diff in differences:
            current += diff
            lowest = min(lowest, current)
            highest = max(highest, current)
        valid_x = (upper - highest) - (lower - lowest) + 1
        return max(0, valid_x)

