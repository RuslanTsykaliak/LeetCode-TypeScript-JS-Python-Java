class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        ArrayList result = new ArrayList<Integer>();

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < m; j++) {
                    if (j % 2 == 0) {
                        result.add(grid[i][j]);
                    }
                }
            } else {
                for (int j = m - 1; j >= 0; j--) {
                    if (j % 2 == 1) {
                        result.add(grid[i][j]);
                    }
                }
            }
        }
        return result;
    }
}