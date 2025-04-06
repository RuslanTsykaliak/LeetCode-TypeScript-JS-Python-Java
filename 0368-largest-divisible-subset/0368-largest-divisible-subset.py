class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = collections.defaultdict(list)
        res[1].append([nums[0]])
        max_len = 1

        for i in range(1, len(nums)):
            num = nums[i]
            added = False
            for length in range(max_len, 0, -1):
                for path in res[length]:
                    if num % path[-1] == 0:
                        new_path = path + [num]
                        new_len = length + 1
                        res[new_len].append(new_path)
                        max_len = max(max_len, new_len)
                        # if new_len > max_len:
                        #     max_len = new_len
                        added = True
                        break
                if added:
                    break
            if not added:
                res[1].append([num])
        return res[max_len][0]
