import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length, n = mat[0].length;

        // Maps to store value-to-row and value-to-column
        Map<Integer, Integer> valueToRow = new HashMap<>();
        Map<Integer, Integer> valueToCol = new HashMap<>();

        // Populate the maps with values from mat
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                valueToRow.put(mat[i][j], i);
                valueToCol.put(mat[i][j], j);
            }
        }

        // Arrays to count painted cells in rows and columns
        int[] rowCounts = new int[m];
        int[] colCounts = new int[n];

        // Process arr using Java Stream API
        return IntStream.range(0, arr.length)
            .filter(i -> {
                int value = arr[i];
                int row = valueToRow.get(value);
                int col = valueToCol.get(value);

                // Increment the painted count for the row and column
                rowCounts[row]++;
                colCounts[col]++;

                // Check if the current row or column is fully painted
                return rowCounts[row] == n || colCounts[col] == m;
            })
            .findFirst()
            .orElse(-1);  // Return -1 if no row or column is fully painted
    }
}