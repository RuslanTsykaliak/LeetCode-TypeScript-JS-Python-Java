class Solution {
    int n;

    public boolean predictTheWinner(int[] nums) {
        n = nums.length;
        int[][] dp = new int[23][23];
        for (int[] arr : dp) {
            Arrays.fill(arr, -1);
        }
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        int first = solve(0, n - 1, totalSum, nums, dp);
        int second = totalSum - first;

        if (first >= second)
            return true;
        else {
            return false;
        }

    }

    int solve(int i, int j, int total, int[] nums, int[][] dp) {
        if (i > j)
            return 0;
        if (i == j)
            return nums[i];

        if (dp[i][j] != -1)
            return dp[i][j];

        int take_i = nums[i] + Math.min(solve(i + 2, j, total, nums, dp), solve(i + 1, j - 1, total, nums, dp));
        int take_j = nums[j] + Math.min(solve(i + 1, j - 1, total, nums, dp), solve(i, j - 2, total, nums, dp));

        return dp[i][j] = Math.max(take_i, take_j);
    }
}