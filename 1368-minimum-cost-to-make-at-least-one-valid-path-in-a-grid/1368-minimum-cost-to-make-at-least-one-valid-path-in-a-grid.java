class Solution {
    public int minCost(int[][] grid) {

        int[][] dirs = new int[][] { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        int m = grid.length, n = grid[0].length;
        boolean visited[][] = new boolean[m][n];

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        pq.add(new int[] { 0, 0, 0 });

        while (!pq.isEmpty()) {
            int[] p = pq.poll();
            if (p[0] == m - 1 && p[1] == n - 1) {
                return p[2];
            }
            if (visited[p[0]][p[1]]) {
                continue;
            }
            visited[p[0]][p[1]] = true;

            for (int d = 0; d < dirs.length; d++) {
                int[] dir = dirs[d];
                int x = p[0] + dir[0], y = p[1] + dir[1];
                if (x > -1 && x < m && y > -1 && y < n && !visited[x][y]) {
                    if (d == grid[p[0]][p[1]] - 1) {
                        pq.offer(new int[] { x, y, p[2] });
                    } else {
                        pq.offer(new int[] { x, y, p[2] + 1 });
                    }
                }
            }

        }

        return -1;
    }
}