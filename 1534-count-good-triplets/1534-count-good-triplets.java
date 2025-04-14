class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        // Input: array and we have three integers a, b, c
        // Output: count of good triplets
        // Conditions:
        // 0 <= i < j < k < arr.length. Satisfaid in Constraints:
        // |arr[i] - arr[j]| <= a
        // |arr[j] - arr[k]| <= b
        // |arr[i] - arr[k]| <= c

        // Algorithm: Brute Force. Enumeratation
        // Data Structures: array, counter, Math.abs() to count the absolute value
        // Math.abs(-3 - 1); // +4 Math.abs(3 - 1) // +2

        int count = 0;
        int n = arr.length;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (Math.abs(arr[i] - arr[j]) > a) continue;
                for (int k = j + 1; k < n; k++) {
                    if (Math.abs(arr[j] - arr[k]) > b) continue;
                    if (Math.abs(arr[i] - arr[k]) <= c) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}