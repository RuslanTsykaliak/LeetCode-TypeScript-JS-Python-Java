class Solution {
    public int maximumDifference(int[] nums) {
        // Store the maximum differece found
        int maxDiff = 0;
        // Keep track of the smallest value encountered so far
        int minVal = nums[0];

        for (int n : nums) {
            // Update max difference if current value gives
            // a larger difference
            maxDiff = Math.max(maxDiff, n - minVal);
            // Update min value if a smaller number is found
            minVal = Math.min(minVal, n);
        }
        // Return -1 if no valid difference was found
        return maxDiff == 0 ? -1 : maxDiff;
    }
}