class Solution {
    public boolean dfs(int[] arr, int idx, boolean[] vis) {
        if (idx < 0 || idx >= arr.length || vis[idx]) {
            return false;
        }
        if (arr[idx] == 0) {
            return true;
        }
        vis[idx] = true;

        return dfs(arr, idx + arr[idx], vis) ||
                dfs(arr, idx - arr[idx], vis);
    }

    public boolean canReach(int[] arr, int start) {
        boolean[] vis = new boolean[arr.length];
        return dfs(arr, start, vis);

    }
}