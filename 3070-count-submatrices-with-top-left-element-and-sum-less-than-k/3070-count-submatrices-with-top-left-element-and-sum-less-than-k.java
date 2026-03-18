class Solution {
    public int countSubmatrices(int[][] grid, int k) {
        int total = 0;
        for (int row = 0; row < grid.length; row++) {
            int sum = 0;
            for (int col = 0; col < grid[row].length; col++) {
                sum += grid[row][col];
                if (sum <= k) {
                    total++;
                }
                if (row < grid.length - 1) {
                    grid[row + 1][col] += grid[row][col];
                }
            }
        }
        return total;
    }
}