class Solution {
    public int maximumCount(int[] nums) {
        // Count of positive and negative integers
        int positive = 0;
        int negative = 0;

        // For each loop
        for (int n : nums) {
            // If integer biger than 1 increase positive
            if (n >= 1) {
                positive++;
            }
            // If integer smaller than 0 than increase negative
            if (n < 0) {
                negative++;
            }
        }

        // Return the maximum between positive and negative integers counts
        return Math.max(positive, negative);
    }
}