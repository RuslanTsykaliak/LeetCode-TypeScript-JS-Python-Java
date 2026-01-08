class Solution {
    Integer dp[][];

    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        dp = new Integer[n][m];
        return solve(0, 0, nums1, nums2);
    }

    public int solve(int i, int j, int nums1[], int nums2[]) {
        if (i >= nums1.length || j >= nums2.length)
            return Integer.MIN_VALUE;

        if (dp[i][j] != null)
            return dp[i][j];

        int product = nums1[i] * nums2[j];
        int include = product + Math.max(0, solve(i + 1, j + 1, nums1, nums2));
        int exclude1 = solve(i + 1, j, nums1, nums2);
        int exclude2 = solve(i, j + 1, nums1, nums2);

        return dp[i][j] = Math.max(include, Math.max(exclude1, exclude2));
    }
}