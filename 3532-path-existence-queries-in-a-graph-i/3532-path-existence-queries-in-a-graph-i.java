class Solution {
    public boolean[] pathExistenceQueries(int n, int[] A, int maxDiff, int[][] queries) {
        int[] g = new int[n];
        for (int i = 1; i < n; i++) {
            g[i] = g[i - 1] + ((A[i] - A[i - 1]) > maxDiff ? 1 : 0);
        }
        int qn = queries.length, qi = 0;
        boolean[] res = new boolean[qn];
        for (int[] q : queries) {
            res[qi++] = g[q[0]] == g[q[1]];
        }
        return res;
    }
}