class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Input: three integers
        # Output: count
        # Conditions:
        # 1. bigger/equal 0 and less than arr.length: 0 <= i < j < k < arr.length
        # 2. (arr[i] - arr[j]) <= a
        # 3. (arr[j] - arr[k]) <= b
        # 4. (arr[i] - arr[k]) <= c

        count = 0

        # Algorithm: Brute Force. Nested loop

        l = len(arr)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count

        
        