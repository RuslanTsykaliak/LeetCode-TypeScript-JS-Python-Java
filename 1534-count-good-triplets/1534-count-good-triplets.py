class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Input: three integers
        # Output: count
        # Conditions:
        # 1. bigger/equal 0 and less than arr.length: 0 <= i < j < k < arr.length
        # 2. (arr[i] - arr[j]) <= a
        # 3. (arr[j] - arr[k]) <= b
        # 4. (arr[i] - arr[k]) <= c

        # Algorithm: Brute Force. Enumeration. Nested loop.
        count = 0
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n -1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) <= c:
                            count += 1
        return count