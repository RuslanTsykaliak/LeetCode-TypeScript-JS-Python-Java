class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Binary Search close to Brute Force
        total = sum(candies)
        if total < k:
            return 0

        l, r = 1, sum(candies) // k
        res = 0

        while l <= r:
            m = (l + r) // 2
            count = 0
            for c in candies:
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            if count >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res

            

        