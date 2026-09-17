class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length,
                ans = n + 1,
                sum = 0;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n);
        for (int l = 0, r = 0; r < n; r++) {
            sum += arr[r];
            while (sum > target)
                sum -= arr[l++];
            dp[r + 1] = dp[r];
            if (sum == target) {
                ans = Math.min(ans, r - l + 1 + dp[l]);
                dp[r + 1] = Math.min(dp[r], r - l + 1);
            }
        }
        return ans == n + 1 ? -1 : ans;
    }
}