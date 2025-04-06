class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        d = {}
        nums = sorted(nums)
        d[1] = [[nums[0]]]
        max_level = 1
        for num in nums[1:]:
            inserted = False
            for level in range(max_level, 0, -1):
                for l in d[level]:
                    if num % l[-1] == 0:
                        if level + 1 > max_level:
                            d[level + 1] = [l + [num]]
                            max_level += 1
                        else:
                            d[level + 1] += [l + [num]]
                        inserted = True
                        break
                if inserted:
                    break
                if level == 1 and l == d[level][-1]:
                    d[1] += [[num]]
        return d[max_level][0]