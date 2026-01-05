class Solution {
    public long maxMatrixSum(int[][] matrix) {

        long totalSum = 0;
        int negativeCount = 0;
        int max_value = Integer.MAX_VALUE;

        for (int i = 0; i < matrix[0].length; i++) {
            for (int j = 0; j < matrix.length; j++) {

                totalSum += Math.abs(matrix[j][i]);

                if (matrix[j][i] < 0)
                    negativeCount++;

                max_value = Math.min(max_value, Math.abs(matrix[j][i]));
            }
        }

        // adjacent elements of matrix and multiply each of them by -1

        if (negativeCount % 2 != 0) {
            totalSum -= 2 * max_value;
        }

        return totalSum;
    }

}