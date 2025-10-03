class Solution {
    public int trapRainWater(int[][] heightMap) {
        int m = heightMap.length;
        int n = heightMap[0].length;

        boolean[][] visited = new boolean[m][n];

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[2] - b[2])); //Min heap

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0 || i == m - 1 || j == n - 1) {
                    pq.add(new int[] { i, j, heightMap[i][j] });
                    visited[i][j] = true;
                }
            }
        }

        int[][] d = new int[][] { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        int ans = 0;

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();

            for (int[] di : d) {
                int nx = curr[0] + di[0];
                int ny = curr[1] + di[1];

                //The boarder is alrady in queue, so it's > 0
                if (nx > 0 && ny > 0 && nx < m - 1 && ny < n - 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    int nextHeight = heightMap[nx][ny];
                    if (nextHeight < curr[2]) {
                        ans += curr[2] - nextHeight;
                        heightMap[nx][ny] = curr[2];
                    }

                    pq.add(new int[] { nx, ny, heightMap[nx][ny] });
                }
            }
        }

        return ans;
    }
}