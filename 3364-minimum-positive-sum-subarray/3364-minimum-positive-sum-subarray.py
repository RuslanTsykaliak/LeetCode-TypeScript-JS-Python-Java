class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        mn = inf
        acc = list(accumulate(nums, initial=0))

        for left in range(len(acc) - l):
            for rght in range(left + l, min(left + r + 1, len(acc))):

                sm = acc[rght] - acc[left]
                if 0 < sm < mn:
                    mn = sm

        return -1 if mn == inf else mn