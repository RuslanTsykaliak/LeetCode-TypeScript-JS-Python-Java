class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Binary Search
        def count_repaired(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time / r))
            return count

        l, r = 1, ranks[0] * cars * cars
        res = 0
        while l <= r:
            m = (l + r) // 2
            repaired = count_repaired(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
