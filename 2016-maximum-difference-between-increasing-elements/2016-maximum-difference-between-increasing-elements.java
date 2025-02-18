class Solution {
    public int maximumDifference(int[] nums) {
        int maxDiff = -1; // Initialize with -1 to handle cases with no valid (i, j)
        int minVal = nums[0]; // Track the smallest value seen so far

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > minVal) {
                maxDiff = Math.max(maxDiff, nums[i] - minVal);
            }
            minVal = Math.min(minVal, nums[i]); // Update minVal after checking maxDiff
        }

        return maxDiff;
    }
}
