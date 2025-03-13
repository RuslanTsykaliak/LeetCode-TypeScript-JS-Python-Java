class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        // 1. Binary Search. O(lon(M) * (N + M)), O(n)
        // 2. Line Sweep
        int n = nums.length, sum = 0, k = 0;
        int[] differenceArray = new int[n + 1];

        // Iterate through nums
        for (int i = 0; i < n; i++) {
            // Iterate through queries while curren index of nums cannot equal zero
            while (sum + differenceArray[i] < nums[i]) {
                k++;

                // Zero array isn't formed after all queries are processed
                if (k > queries.length) {
                    return -1;
                }

                int left = queries[k - 1][0], right = queries[k - 1][1], val = queries[k - 1][2];

                // Process start and end of range
                if (right >= i) {
                    differenceArray[Math.max(left, i)] += val;
                    differenceArray[right + 1] -= val;
                }
            }
            // Update prefix sum at current index
            sum += differenceArray[i];
        }
        return k;
    }
}