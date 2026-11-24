class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # Brute force with running values
        best = 0
        n = len(nums)
        
        for i in range(n):
            p, g, l = 1, 0, 1    # product, gcd, lcm so far
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = gcd(g, x)    # gcd(0, x) = x, so 0 is a safe start
                l = lcm(l, x)
                if p == g * l:
                    best = max(best, j - i + 1)
                if p > 25200:    # can never match again, stop early
                    break
        return best