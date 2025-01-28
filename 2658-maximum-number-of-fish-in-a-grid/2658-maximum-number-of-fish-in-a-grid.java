class Solution {
    public int findMaxFish(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int maxFish = 0;
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    maxFish = Math.max(maxFish, bfs(grid, visited, i, j));
                }
            }
        }
        return maxFish;
    }

    private int bfs(int[][] grid, boolean[][] visited, int x, int y) {
        int[] drow = { -1, 0, 1, 0 }; // Row movement
        int[] dcol = { 0, 1, 0, -1 }; // Column movement

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { x, y });
        visited[x][y] = true;
        int fishCount = 0;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0];
            int c = cell[1];
            fishCount += grid[r][c];

            for (int i = 0; i < 4; i++) {

                int nrow = r + drow[i];
                int ncol = c + dcol[i];
                if (nrow >= 0 && nrow < grid.length && ncol >= 0 && ncol < grid[0].length
                        && grid[nrow][ncol] > 0 && !visited[nrow][ncol]) {
                    queue.add(new int[] { nrow, ncol });
                    visited[nrow][ncol] = true;
                }
            }
        }
        return fishCount;
    }
}