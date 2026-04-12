class Solution {

    private int getDistance(int p, int q) {
        int x1 = p / 6;
        int y1 = p % 6;
        int x2 = q / 6;
        int y2 = q % 6;
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    public int minimumDistance(String word) {
        int n = word.length();
        int[][] dp = new int[n][26];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], Integer.MAX_VALUE / 2);
        }
        Arrays.fill(dp[0], 0);

        for (int i = 1; i < n; i++) {
            int cur = word.charAt(i) - 'A';
            int prev = word.charAt(i - 1) - 'A';
            int d = getDistance(prev, cur);

            for (int j = 0; j < 26; j++) {
                dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + d);
                if (prev == j) {
                    for (int k = 0; k < 26; k++) {
                        int d0 = getDistance(k, cur);
                        dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + d0);
                    }
                }
            }
        }

        int ans = Integer.MAX_VALUE / 2;
        for (int value : dp[n - 1]) {
            ans = Math.min(ans, value);
        }
        return ans;
    }
}