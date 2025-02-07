class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        HashMap<Integer, HashSet<Integer>> colors = new HashMap<>();
        HashMap<Integer, Integer> balls = new HashMap<>();
        int q = queries.length;
        int ans[] = new int[q];
        int i = 0, x, y, c;
        for (int arr[] : queries) {
            x = arr[0];
            y = arr[1];
            if (balls.containsKey(x)) {
                c = balls.get(x);
                colors.get(c).remove(x);
                if (colors.get(c).size() == 0) {
                    colors.remove(c);
                }
            }
            balls.put(x, y);
            if (!colors.containsKey(y)) {
                colors.put(y, new HashSet<>());
            }
            colors.get(y).add(x);
            ans[i++] = colors.size();
        }
        return ans;
    }
}