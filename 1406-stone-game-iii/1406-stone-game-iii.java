class Solution {
    public String stoneGameIII(int[] stoneValue) {

        int n = stoneValue.length;

        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MIN_VALUE);

        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--) {

            int take = 0;

            for (int k = 0; k < 3 && i + k < n; k++) {

                take += stoneValue[i + k];

                dp[i] = Math.max(
                        dp[i],
                        take - dp[i + k + 1]);
            }
        }

        if (dp[0] > 0)
            return "Alice";

        if (dp[0] < 0)
            return "Bob";

        return "Tie";
    }
}