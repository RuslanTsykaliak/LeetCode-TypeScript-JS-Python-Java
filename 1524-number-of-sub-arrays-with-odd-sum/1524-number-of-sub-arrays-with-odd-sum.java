class Solution {

    public int numOfSubarrays(int[] arr) {
        final int MOD = (int) (1e9 + 7);
        int n = arr.length;
        int count = 0;

        // Generate all possible subarrays
        for (int startIndex = 0; startIndex < n; startIndex++) {
            int currentSum = 0;
            // Iterate through each subarray starting at startIndex
            for (int endIndex = startIndex; endIndex < n; endIndex++) {
                currentSum += arr[endIndex];
                // Check if the sum is odd
                if (currentSum % 2 != 0) {
                    count++;
                }
            }
        }

        return count % MOD;
    }
}