class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        // Input: three integers
        // Output: count of triplets that follow these conditions:
        // 0 <= i < j < k < arr.length
        // |arr[i] - arr[j]| <= a
        // |arr[j] - arr[k]| <= b
        // |arr[i] - arr[k]| <= c
        // where |x| denotes the absolute value. For example,
        // Math.abs(-3 - 1) returns 4, and Math.abs(3 - 1) returns 2.

        // Algorithms: Enumerate (Brute Force)
        // Data Structures: Nested loops; use Math.abs for absolute value computations.

        int count = 0;
        int n = arr.length;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (Math.abs(arr[i] - arr[j]) > a) {
                    continue;
                }
                for (int k = j + 1; k < n; k++) {
                    if (Math.abs(arr[j] - arr[k]) > b) {
                        continue;
                    }
                    if (Math.abs(arr[i] - arr[k]) <= c) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
