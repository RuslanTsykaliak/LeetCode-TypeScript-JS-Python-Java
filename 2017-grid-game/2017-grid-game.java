class Solution {
    public long gridGame(int[][] g) {
        long top = 0;
            long bottom = 0;
            int n = g[0].length;

            for(int i = 0; i < n; i++){
                top += g[0][i];
            }

            long res = Long.MAX_VALUE;

            for(int i = 0; i < n; i++){
                top -= g[0][i];
                res = Math.min(res, Math.max(top, bottom));
                bottom += g[1][i];
            }

            return res;
        }
}