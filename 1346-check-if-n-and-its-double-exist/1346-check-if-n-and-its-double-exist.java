class Solution {
    public boolean checkIfExist(int[] arr) {
        // Input one array of integer
        // Output boolean
        // Conditions:
        // i != j
        // 0 <= i, j < arr.length
        // arr[i] == 2 * arr[j]

        // Nested Loops

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == 2 * arr[j] && i != j) {
                    return true;
                }
            }
        }

        return false;
    }
}