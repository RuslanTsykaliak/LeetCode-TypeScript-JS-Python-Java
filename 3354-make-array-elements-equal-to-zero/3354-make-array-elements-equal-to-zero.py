class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            
            for direction in [-1, 1]:  # -1 is left, 1 is right
                curr = i
                dir = direction
                tmp = nums[:]  # Make a copy so we don't mess up the original
                
                while 0 <= curr < n:
                    if tmp[curr] == 0:
                        curr += dir
                    elif tmp[curr] > 0:
                        tmp[curr] -= 1
                        dir *= -1      # reverse direction
                        curr += dir
                # At the end, check if all is zero
                if all(x == 0 for x in tmp):
                    res += 1
        return res