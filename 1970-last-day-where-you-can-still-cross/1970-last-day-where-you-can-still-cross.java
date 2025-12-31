class Solution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        int start = 0;
        int end = cells.length - 1;
        int ans = 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (isTraversalPossible(row, col, mid, cells)) {
                ans = mid;
                start = mid + 1;
            } else
                end = mid - 1;
        }
        return ans;
    }

    public boolean isTraversalPossible(int row, int col, int mid, int[][] cells) {
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < mid; i++) {
            int[] cell = cells[i];
            visited[cell[0] - 1][cell[1] - 1] = true;
        }
        int dx[] = { -1, 0, 1, 0 };
        int dy[] = { 0, 1, 0, -1 };
        Set<Integer> set = new HashSet<>();
        Queue<int[]> q = new LinkedList<>();
        boolean flag = false;
        for (int i = 0; i < col; i++) {
            if (visited[0][i] == false) {
                flag = true;
                q.add(new int[] { 0, i });
                set.add(i);
            }
        }
        if (flag == false)
            return false;
        while (!q.isEmpty()) {
            int k = q.size();
            for (int i = 0; i < k; i++) {
                int[] temp = q.poll();
                int x = temp[0];
                int y = temp[1];
                for (int j = 0; j < 4; j++) {
                    int newX = x + dx[j];
                    int newY = y + dy[j];
                    int val = newX * col + newY;
                    if (newX >= 0 && newX < row && newY >= 0 && newY < col && !set.contains(val)
                            && visited[newX][newY] == false) {
                        if (newX == row - 1)
                            return true;
                        set.add(val);
                        q.add(new int[] { newX, newY });
                    }
                }
            }
        }
        return false;
    }
}