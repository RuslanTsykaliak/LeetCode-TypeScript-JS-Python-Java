class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++)
            order[i] = i;
        Arrays.sort(order, (a, b) -> nums[a] - nums[b]);

        int[] pos = new int[n];
        int[] val = new int[n];
        for (int i = 0; i < n; i++) {
            pos[order[i]] = i;
            val[i] = nums[order[i]];
        }

        int[] reach = new int[n];
        for (int i = 0, j = 0; i < n; i++) {
            if (j < i)
                j = i;
            while (j + 1 < n && val[j + 1] - val[i] <= maxDiff)
                j++;
            reach[i] = j;
        }

        int[] comp = new int[n];
        for (int i = 1; i < n; i++)
            comp[i] = comp[i - 1] + (val[i] - val[i - 1] > maxDiff ? 1 : 0);

        int LOG = 1;
        while ((1 << LOG) < n)
            LOG++;
        int[][] jump = new int[LOG][n];
        jump[0] = reach.clone();
        for (int k = 1; k < LOG; k++)
            for (int i = 0; i < n; i++)
                jump[k][i] = jump[k - 1][jump[k - 1][i]];

        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int pu = pos[queries[qi][0]], pv = pos[queries[qi][1]];
            if (comp[pu] != comp[pv]) {
                ans[qi] = -1;
                continue;
            }
            if (pu == pv) {
                ans[qi] = 0;
                continue;
            }
            if (pu > pv) {
                int t = pu;
                pu = pv;
                pv = t;
            }
            int dist = 0, cur = pu;
            for (int k = LOG - 1; k >= 0; k--) {
                if (jump[k][cur] < pv) {
                    cur = jump[k][cur];
                    dist += 1 << k;
                }
            }
            if (cur < pv)
                dist++;
            ans[qi] = dist;
        }
        return ans;
    }
}